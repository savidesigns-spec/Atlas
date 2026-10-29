# Architecture — broker, ledger, agent back office

The system has two front doors:
- the **user app** (web)
- the **agent back office** (MCP + REST + chat bots)

Both drive the same core: a **job router** that picks a provider, and a **credit ledger**
that never lets a job run without a hold on the balance.

```
 Web app ─┐                                   ┌─ fal.ai
 MCP  ────┤   Auth + agent keys               ├─ Google Vertex / Gemini API (Veo, Nano Banana)
 REST ────┼──▶ (scopes, spend caps) ──▶ Jobs ─┼─ BytePlus ModelArk (Seedance)
 Slack/   │                            API    ├─ Kling API
 Discord ─┘                             │     ├─ Replicate
                                        │     └─ Self-hosted GPU lane (open weights)
                     ┌──────────────────┼──────────────────┐
                     ▼                  ▼                  ▼
               Credit ledger      Queue (realtime /    Object storage
               (Postgres)         saver lanes)         (R2) + CDN
                     │                  │
                     ▼                  ▼
                 Stripe            Webhooks → users, agents, workflows
```

## 1. Stack (recommended)
| Layer | Pick | Why |
|---|---|---|
| Web | Next.js (App Router) on Vercel | Already connected to this workspace |
| DB | Postgres (Supabase or Neon) | Ledger needs real transactions |
| Queue / workflows | Inngest or Temporal | Durable steps, retries, cron for automations |
| Storage | Cloudflare R2 | No egress fees, which matters for video |
| Billing | Stripe Billing + Checkout | Subscriptions, one-time top-ups, Customer Portal for one-click cancel |
| Moderation | Provider moderation + an image/text classifier pass | Required to keep provider and Stripe accounts |

## 2. Credit ledger (the part that must be right)
Append-only table `ledger_entries(id, account_id, kind, credits, job_id, created_at)`.
`kind` is one of `grant | topup | hold | capture | release | refund | expire | adjust`.

Every job follows **quote → hold → run → capture or release**:
1. **Quote.** `price = ceil(wholesale × markup × lane_discount / face_value)`, using the
   price table *at submit time* so a later provider price change never rebills a job.
2. **Hold.** In one transaction:
   - check `available = sum(entries) − open_holds ≥ price`
   - check the agent key's caps (per-job and month-to-date)
   - insert a `hold`
3. **Run.** The router dispatches the job.
4. **Settle.**
   - On success: `capture` (hold → spent).
   - On provider error, a moderation block, or a timeout: `release`. This is the
     automatic failed-gen refund from the plan.

Credits are spent in this order, oldest first:
1. plan grant
2. rollover
3. top-up

At renewal, the unused grant over the 1x rollover cap gets an `expire` entry. Top-ups
never expire while the subscription is active.

## 3. Router
For each `(model, params)` the router has an ordered list of provider adapters, each
with its live price, health (error rate, p95 latency) and a lane flag.
- **Realtime lane:** cheapest healthy provider under the latency SLO.
- **Saver lane:** batch/off-peak endpoints and the self-hosted GPU lane. Jobs may wait
  up to 24h. Charged at 50%.
- **"Auto" model:** a small policy picks the cheapest model meeting the job's quality
  tier (fast / standard / best) for its type (image, i2v, t2v, edit).
- **Failover:** a provider 5xx or timeout retries on the next adapter. The user is
  charged once, at the quoted price.

Adapter interface: `quote(params) · submit(params) → provider_job_id · poll(id) ·
cancel(id) · normalize(output) → asset`.

## 4. Agent back office
- **Agent keys:** `ak_live_…`, scoped to one account. Each key has:
  - an allowed-tools list
  - `max_credits_per_job`
  - `max_credits_per_month`
  - an optional `requires_approval_over` threshold (pings the owner in the app/Slack)
  - an IP allowlist (optional)
- **Remote MCP server** (Streamable HTTP, OAuth 2.1 for Claude connectors; bearer
  agent key for headless agents). Tools are in `backoffice/mcp-tools.json`.
- **REST** mirrors the MCP tools one-to-one: `/v1/quote`, `/v1/jobs`, `/v1/workflows/:id/run`, …
- **Webhooks:**
  - `job.completed`
  - `job.failed`
  - `workflow.run.completed`
  - `balance.low`

  Each payload is HMAC-signed.
- **Chat connectors:** Slack / Discord / Telegram apps are thin clients over the same
  task API. Each workspace binds to one agent key, so caps apply.
- **Audit log:** every call, its key, tool, credits held/captured and result. The owner
  dashboard shows it.

## 5. Workflows ("Automate" tab)
A workflow is a stored list of steps plus a trigger. Steps:
- `generate`
- `upscale`
- `reframe`
- `caption`
- `publish_draft` (TikTok/IG/Shopify media)
- `notify`
- `ask_llm` (Claude writes prompts or scripts)

Triggers:
- `cron`
- `webhook`
- `store.product.created`
- `manual`
- `agent`

Workflows default to the saver lane. Each run pre-quotes its whole step list and holds
the total before step 1, so a run never dies halfway on an empty balance.

## 6. Store connectors (the wedge)
- **Shopify:** an app with `read_products`, `write_files` (to attach generated media),
  and webhooks for `products/create`.
- **WooCommerce:** REST keys plus a webhook on product publish.

Both feed the `store.product.created` trigger and the "Turn this product into ads"
templates.

## 7. Owner metrics (from the ledger + Stripe)
| Group | Metrics |
|---|---|
| Revenue | MRR, ARPU, top-up revenue |
| Margin | gross margin per model and per provider (captured credits × face vs wholesale billed) |
| Credits | breakage, rollover liability (unspent credits = deferred revenue) |
| Reliability | failed-job rate per provider, refunds released |
| Agents | spend by agent key |
| Retention | cohort churn |
