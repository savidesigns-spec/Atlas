# AI Video Broker — Business, Sales & Marketing Plan

*Working name: TBD. Drafted 2026-10-29. Confidence tags: **[Certain]** = hard evidence
(live data or our own math), **[Likely]** = strong inference from multiple sources,
**[Guessing]** = assumption to be replaced with real data.*

---

## 0. The part you won't like (read first)

1. **"Higgsfield's price, 5x the output" loses money on every active user.** [Certain]
   Higgsfield's own live pricing (pulled through their MCP server today) sells ~200
   Kling 3.0 videos for 1,000 credits on a $39/mo plan, about **$0.195 a video**. The
   public API price for that clip is **~$0.56**. Five times that output at $39 costs us
   $560 at full use, and **we break even only if users touch less than 6.7% of their
   allowance.** See `model/economics.py`, section 3.
2. **At public API prices we are ~5x *more* expensive than Higgsfield on premium video,
   not 5x cheaper.** [Certain, on today's list prices] Higgsfield is at roughly
   $1B annualized revenue [Likely]. Volume like that buys wholesale rates we can't get on
   day one, so they can sell below list price.
3. **"MCP + agents + automation" isn't a moat by itself.** [Certain] Higgsfield already
   ships an MCP server with generation, scheduled jobs ("Supercomputer", 2–10 scheduled
   jobs per plan), TikTok publishing and website building. I used it to research this plan.

**So the plan below doesn't try to be cheaper on premium compute.** It wins on what costs
us little and what Higgsfield does badly:

- honest billing: no expiring credits, automatic refunds when a generation fails, no
  "unlimited" promotions with hidden limits
- a simpler product
- 5x more *automation, storage, concurrency and credit lifetime*
- a "Saver queue" that's half price for jobs that can wait
- a store-connected workflow wedge for small e-commerce brands

The cheap lane comes first. Premium-model prices come down as wholesale contracts land.

---

## 1. Executive summary

**What it is:** a single subscription that brokers the latest image and video models
(Seedance, Kling, Veo, Nano Banana, Wan, Grok, MiniMax and others) behind one clean
interface. Users pay a monthly fee and buy top-up points when they need more. Everything
the web app can do is also exposed to AI agents through an MCP server and a REST API, so
users (and their Claude/ChatGPT/Slack bots) can run fully automated content workflows.

**Who it's for (in order):**
1. Small e-commerce brands (Shopify/WooCommerce) that need weekly product ads. This is
   the wedge. We already run one, Hglif3.com, so we have a test customer on day one.
2. Solo creators and UGC freelancers who find Higgsfield noisy and confusing.
3. Developers and agencies who want one API/MCP key for every model instead of six vendor
   accounts.

**How it makes money:**
- subscriptions ($19 / $49 / $129)
- top-up packs at a 45–51% margin
- later, an agency tier and API usage

Credits are priced at **wholesale × 1.6**. The plans run at a **57–60% gross margin at
65% utilization** and still clear **40% if every credit gets used** [Certain, given the
cost inputs].

**What we need:** a 2–3 person build team for about 12 weeks to reach a paid beta. Capital
is mostly prepaid model inventory and paid acquisition. See section 12.

---

## 2. Market: who is making money

| Company | Model | Revenue signal | Confidence |
|---|---|---|---|
| **Higgsfield** | Aggregator + own models (Soul, Cinema Studio), viral presets | ~$1B annualized (Sep 2026, company claim); $200M (Jan 2026); $50M (Sep 2025). Raised at $5.4B. | Likely; self-reported |
| **Magnific (ex-Freepik)** | Stock library → AI suite aggregator | $230M ARR, about half from AI video; 1M+ paid subs | Likely; company-announced |
| **OpenArt** | Aggregator, templates, character consistency | ~$70M ARR (2025), profitable | Likely; Sacra estimate |
| **Krea** | Real-time aggregator | $9–$105/mo; no revenue figure found | — |
| **Google Flow (Veo)** | Model owner, direct | $4.99 to $199.99/mo tiers | Certain on pricing |
| **Kling / Runway / Pika** | Model owners, direct | $7–$144/mo tiers | Likely |

**Takeaways:**
- **Aggregators are out-earning most model owners on consumer revenue.** [Likely] Users
  don't want six subscriptions. The broker model is proven.
- **Growth came from viral presets and templates, not raw model access.** [Likely]
  Higgsfield's catalog is built around one-click "effects", "Genjutsu" motion/object
  swaps, AI influencers and Marketing Studio ads. People buy outcomes, not models.
- **The market has room for a simpler, more honest player.** [Likely] Higgsfield
  complaints cluster on:
  - refunds being refused after even one credit is used, with a fee of up to 6%
  - charges after cancellation
  - credits burning fast
  - "unlimited" promotions that are time-boxed (7-day, 365-day) and model-specific

---

## 3. Higgsfield teardown

### What they sell (live config, 2026-10-29) [Certain]

| Plan | Price | Credits/mo | Effective $/credit |
|---|---|---|---|
| Plus (annual) | $39/mo | 1,000 | $0.039 |
| Ultra (monthly) | $129/mo | 3,000 | $0.043 |
| Ultra (annual) | $99/mo | 3,000 | $0.033 |
| Top-up 500 → 4,000 | $29 → $210.53 | one-time, **expires in 90 days** | $0.059 → $0.053 |

**Upsell stack on every plan:**
- "7-Day Unlimited" Nano Banana 2 / Pro / Kling 3.0
- "365-Day Unlimited" Seedream / Flux.2 / GPT Image / Nano Banana
- thousands of "free gens" on their own Soul model
- 6–8 parallel jobs
- 2–5 GB storage
- 2–10 scheduled jobs
- auto-refill pushed as the default way to buy credits

### What actually sells

[Likely] **Nano Banana Pro images and Kling/Seedance short video**, packaged as presets.
Their own tooltips sell those two first: "= 600 Nano Banana Pro generations", "~200
Kling 3.0 videos". Third-party coverage points to Nano Banana Pro as the most-used tool
since late 2025. Seedance 2.0 "full access" is the current headline feature. I found no
public sales breakdown; this comes from what they put front and center. [Guessing on
exact ranking]

### How they hit those prices

[Likely] Higgsfield prices Nano Banana Pro at ~$0.065/image, roughly **Google's batch
rate ($0.067)** and half the real-time list price ($0.134). Kling 3.0 sits at about a
third of fal's list price. The likely mechanisms:
- committed-volume contracts
- batch/off-peak inference
- breakage (credits bought but never used, helped by the 90-day expiry)
- "unlimited" offers on cheap or self-owned models that make the plan feel bigger than
  its compute cost

### Where they're beatable

| Pain | Our answer |
|---|---|
| ~80 video models, presets, "Genjutsu", "Supercomputer", contests. Overwhelming. | 3 tabs: **Create · Automate · Library**. Show 8 curated models, with "advanced" behind a toggle. |
| Credits expire (top-ups after 90 days) | Plan credits roll over up to 1x; top-ups never expire while subscribed |
| No refund once one credit is used | Failed or blocked generations refund automatically. 7-day no-questions refund if you've used under 20% of your credits. |
| "Unlimited" that isn't | No unlimited. A price receipt on every generation: model, seconds, credits, $ |
| Cancellation friction | One-click cancel in settings. Confirmation email. Prorated. |
| Scheduled jobs capped at 2–10 | 10–250 automations by plan, plus agent keys with spend caps |

---

## 4. Competitor comparison: aggregators with an agent/MCP surface

| | Higgsfield | Magnific (Freepik) | OpenArt | Krea | **Us** |
|---|---|---|---|---|---|
| Entry paid price | $39/mo (annual) | ~$9–$24 [Likely] | ~$14 [Guessing] | $9 | **$19** |
| Models | 80+ video, own + 3rd party | Broad 3rd party | Broad 3rd party | Broad + real-time | 8 curated + advanced |
| Own MCP server | **Yes** (gen, jobs, publishing, sites) | Unknown | Unknown | Unknown | **Yes, day one** |
| Scheduled automation | 2–10 jobs | — | — | — | **10–250 automations** |
| Agent API keys with spend caps | No (account-level) | — | — | — | **Yes, per agent** |
| Store connector (Shopify/Woo) | Product URL import in Marketing Studio | — | — | — | **Catalog sync → auto ads** |
| Credit expiry | 90 days on top-ups | Monthly | Monthly | Daily units | **Rollover; top-ups don't expire** |
| Failed-gen refund | Unclear | Unclear | Unclear | Unclear | **Automatic** |
| Price transparency | Credits only | Credits only | Credits only | Units | **$ receipt per job** |

*"Unknown" = I found no public MCP server for that product as of today; verify before
quoting it in marketing.*

---

## 5. Positioning: what "5x more" means in practice

You asked for similar pricing with 5x more. Giving 5x more *compute* bankrupts us
(section 0). Here's where we can honestly give 5x at the same price:

| "5x" claim | Higgsfield Plus ($39) | Us, Pro ($49) | Cost to us |
|---|---|---|---|
| Automations / scheduled jobs | 2 | **50** (25x) | ~0, it's a queue |
| Storage | 2 GB | **100 GB** (50x) | ~$1.50/mo on R2 |
| Credit lifetime | 90 days (top-ups) | **No expiry while subscribed** | Less breakage. We give it up on purpose. |
| Budget-lane volume | — | **5x more Veo Lite / Nano Banana 2 / Saver-queue output per dollar** than our own premium lane | Built into the pricing |
| Agent seats | 1 account | **5 agent keys** | ~0 |

**Tagline direction:** *"Every top AI video model. One honest price. Automate the rest."*

---

## 6. Product

### 6.1 User app (three tabs)
- **Create:** a prompt box, model picker (Auto / Fast & cheap / Best quality / pick
  exact), aspect ratio, duration. Live credit + $ quote before you press Generate.
  Reference images, start/end frames.
- **Automate:** workflow templates, e.g.:
  - "Every Monday: take my 5 newest Shopify products → 3 ad variants each → post to TikTok drafts"
  - "When a new product goes live → hero image + 9:16 video"
  - "Turn this product URL into a 15s UGC ad"

  The builder is a step list, not a node graph. Saver-queue toggle per workflow.
- **Library:** every output with its receipt, re-run / remix / upscale, folders, share link.
- **Billing panel:** balance, rollover, top-up, one-click cancel, usage by model.

### 6.2 Owner (admin) back office
- revenue
- margin by model and provider
- provider wallet balances
- failed-job rate
- refunds issued
- abuse flags
- cohort churn

### 6.3 Agent back office (separate from the user app)
A dedicated console just for bots/agents. Each agent gets its own key with:
- a **monthly credit cap and per-job cap** (it mirrors the Apogee Station guardrail:
  nothing spends without a limit set by a human)
- an allowed-tools list (e.g. "can quote and generate, can't buy top-ups")
- a task queue, so an agent can post a task, poll it, and get a webhook on completion
- an audit log of every call

Exposed three ways:
1. **Remote MCP server.** Add it as a custom connector in Claude (claude.ai / Claude Code
   / Desktop) or in any MCP-capable client.
2. **REST + webhooks** for Zapier/Make/n8n and custom code.
3. **Chat connectors:** Slack, Discord and Telegram bots that wrap the same task API
   ("/video 9:16 product spin of SKU-123").

Spec: `backoffice/mcp-tools.json`. Architecture: `ARCHITECTURE.md`. Clickable prototype
of all three dashboards: `dashboards/index.html`.

---

## 7. Pricing & unit economics

Run `python3 model/economics.py` to regenerate the tables below from `model/pricing.json`.

### Plans
| Plan | Price | Credits | Concurrency | Storage | Automations | Agent keys |
|---|---|---|---|---|---|---|
| Free | $0 | 150 one-time | 1 | 2 GB | 1 | 0 |
| Creator | $19 | 1,500 | 4 | 25 GB | 10 | 1 |
| Pro | $49 | 4,200 | 8 | 100 GB | 50 | 5 |
| Studio | $129 | 11,500 | 16 | 500 GB | 250 | 25 |
| Top-ups | $14 / $39 / $119 | 1k / 3k / 10k | | | | |

### Gross margin
Blended wholesale cost is $0.0062 per credit. [Certain math; Guessing usage mix]

| Plan | @40% used | @65% used | @100% used |
|---|---|---|---|
| Creator | 69% | 57% | 40% |
| Pro | 73% | 59% | 41% |
| Studio | 74% | 60% | 41% |
| Top-ups | 45–51% | | |

Free tier costs about **$1.85 per signup**, so cap it at one per verified phone or card.

### Price per output (Pro plan)

| Output | Real-time | Saver queue |
|---|---|---|
| Veo 3.1 Lite 5s | **$0.28** | $0.14 |
| Nano Banana 2 | **$0.13** | $0.07 |
| Nano Banana Pro 2K | **$0.26** | $0.13 |
| Kling 3.0 5s | **$1.05** | $0.53 |
| Seedance 2.0 Fast 5s | **$2.26** | $1.13 |

Higgsfield sells Kling 3.0 at about $0.195 and Nano Banana Pro at about $0.065. This is
the gap sections 0 and 8 deal with.

---

## 8. Closing the premium-price gap

In order of impact:

1. **Saver queue (day one).** Route non-urgent and automated jobs to batch/off-peak
   endpoints. Google's batch rate is half of real-time for Nano Banana [Likely].
   Automations are the natural user of this, since nobody waits on a Monday-morning job.
2. **Multi-provider routing.** The same model is priced differently by the model owner,
   fal, Replicate, and resellers [Likely]. The router picks the cheapest healthy provider
   per job (`ARCHITECTURE.md` §3).
3. **Direct contracts** once spend passes about $20–50k/mo: BytePlus ModelArk (Seedance),
   Kling API, Vertex AI (Veo/Gemini). Expect 20–50% off list with committed spend.
   [Guessing on the discount size]
4. **Self-hosted open-weights models** (Wan 2.x/3.x where licenses allow) on rented GPUs
   for the budget lane. Likely under $0.10 per 5s clip at good utilization, but this
   needs a benchmark before we promise it. [Guessing]
5. **Default to "Auto".** Most users can't tell Kling 3.0 from Kling 2.5 Turbo for a
   product spin. "Auto" sends each job to the cheapest model that meets the quality bar.

We only match Higgsfield on premium models after steps 3–4. Until then, marketing leads
on honesty, simplicity and automation, never on "cheapest Kling".

---

## 9. Sales plan

| Segment | Motion | Offer | Goal (month 6) |
|---|---|---|---|
| Small e-com brands | Self-serve + Shopify/Woo app listing + founder-led demos | "Connect your store, get 20 ad videos this week." 14-day Pro trial with a card. | 300 paid |
| Creators / UGC freelancers | Self-serve, affiliates | Creator plan, template gallery | 900 paid |
| Agencies | Founder-led sales, Studio + seats | Studio at $129 + $29/seat, white-label share links | 25 accounts |
| Developers / agent builders | Docs, MCP registry listings | Free key with 150 credits, pay-as-you-go top-ups | 150 active keys |

**Funnel targets:** [Guessing; replace after 30 days of data]
- visitor → signup: 6%
- signup → paid: 8%
- monthly logo churn: 8% on Creator, 5% on Pro/Studio

**Affiliate program:** 20% recurring for 12 months (not 30%+). At a ~58% gross margin a
30% cut leaves too little room for paid ads.

---

## 10. Marketing plan (first 90 days)

| Weeks | Focus | Actions |
|---|---|---|
| 1–4 | **Private beta** | 50 users from the Hglif3 audience + 20 hand-picked UGC creators. Free Pro for feedback and content rights. Make every launch asset with the product itself. |
| 3–8 | **Content engine** | 3 short-form posts a day (TikTok/Reels/Shorts), each showing prompt → result → *the receipt*. Recurring formats: "Higgsfield vs us: same prompt, what you actually pay" and "This workflow made 20 ads while I slept." |
| 4–10 | **SEO + comparison pages** | Pages for "Higgsfield alternative", "Seedance 2.0 price", "Kling 3.0 API", "Nano Banana Pro without subscription", "AI product video for Shopify". A public live model price index, updated weekly from `pricing.json`. |
| 6–12 | **Launch** | Product Hunt, Shopify App Store, WooCommerce marketplace. MCP registries and Claude connector directory submission. Discord community with weekly prompt contests (prizes in credits, which cost us about 62¢ per $1 of face value). |
| 8–12 | **Paid** | $3–5k/mo test budget on TikTok + Meta, retargeting site visitors with receipt-style creatives. Kill any channel above $60 CAC on Creator or $120 on Pro. [Guessing thresholds] |
| ongoing | **Affiliates** | Recruit 30 AI-tool YouTubers/TikTokers at 20% recurring. Give them their own template pack. |

**Messaging pillars:**
1. Every top model, one price.
2. You see exactly what you pay.
3. Credits don't vanish.
4. Your agents can run it while you sleep.

---

## 11. Operations & team

- **Founder:** product, partnerships, sales to brands and agencies.
- **Full-stack engineer:** web app, billing, ledger.
- **Backend/infra engineer** (or contractor): provider adapters, queue, MCP server, GPU lane.
- **Part-time:** content creator/community manager from week 3, support via a docs bot
  + email.
- **Trust & safety:** run each provider's moderation on every prompt and output, plus
  our own blocklist. NSFW and real-person deepfakes are blocked by default. Keep an audit
  trail per job. This is mandatory for staying on Stripe and keeping provider accounts.
- **Legal:**
  - ToS with content-rights language passed through from each provider's terms
  - DMCA agent
  - a refund policy that matches the marketing
  - state auto-renewal law compliance (clear disclosure, easy online cancel)

---

## 12. Financials (12-month scenarios)

[Guessing on volumes; Certain on the arithmetic.] Inputs:
- Plan mix: 60% Creator / 30% Pro / 10% Studio, for an ARPU of $39. With top-ups (~15%
  uplift) that's about **$45 ARPU**.
- Gross margin: 58% at 65% utilization.

| Month 12 | Conservative | Base | Aggressive |
|---|---|---|---|
| Paid subscribers | 400 | 1,500 | 5,000 |
| MRR | $18k | $67.5k | $225k |
| Gross profit / mo | $10.4k | $39k | $130k |
| Marketing / mo | $4k | $15k | $50k |
| Team + tools / mo | $25k | $35k | $60k |
| **Monthly net** | **−$18.6k** | **−$11k** | **+$20k** |

**Starting capital:** about **$250–350k** covers 12 months of the base case. That breaks
down as:
- team
- $40–60k of prepaid provider credit (needed for wholesale tiers)
- paid acquisition

Bootstrapping on a two-founder team with no salaries cuts this to roughly $60–90k.

---

## 13. Risks

| Risk | Likelihood | Mitigation |
|---|---|---|
| Higgsfield/Magnific cut prices again | High | Don't compete on premium price. Compete on automation and honesty. |
| Provider raises prices or deprecates a model (e.g. a fal Veo 3 endpoint is flagged for deprecation on 2026-11-17) | High | Price table is config. Router fails over. Credits are priced per job at submit time. |
| A provider bans resale | Medium | Use providers whose terms allow API resale. Read each ToS before launch. Keep 2+ providers per flagship model. |
| Abuse (free-tier farming, deepfakes, chargebacks) | High | Card/phone verification. Moderation on every job. Spend caps. Stripe Radar. |
| Margin squeeze if power users burn 100% | Medium | Still 40% at full use. Concurrency limits. Saver queue nudges. |
| Being "just a wrapper" | High | The moat is workflows, store connectors and agent keys plus saved templates. That's what makes switching painful. |

---

## 14. Milestones

| Week | Milestone |
|---|---|
| 0–2 | Provider accounts (fal + Google + one direct), Stripe, ledger, 6 models live internally |
| 3–6 | Create + Library tabs, billing, private beta (50 users) |
| 7–9 | Automate tab, 5 templates, Shopify/Woo connector, agent keys + MCP server |
| 10–12 | Public launch, Saver queue, affiliate program, owner dashboard v1 |
| 13–24 | Direct contracts, self-hosted budget lane, agency tier, Slack/Discord bots |

---

## Sources
- Higgsfield live plans & model catalog: Higgsfield MCP server (`show_plans_and_credits`, `models_explore`), 2026-10-29
- [Higgsfield ARR coverage, ARR Club](https://www.arr.club/higgsfield/higgsfield-surpasses-700m-arr-with-400m-series-b-at-5-4b-valuation) · [OfficeChai on $1B ARR](https://officechai.com/ai/ai-video-platform-higgsfield-says-it-has-gone-from-1-million-arr-to-1-billion-arr-faster-than-anthropic-or-openai/) · [Sacra, $230M ARR](https://sacra.com/research/higgsfield-at-230m-arr/) · [TechTimes, $500M](https://techtimes.com/articles/319394/20260630/ai-video-startup-higgsfield-hits-500m-revenue-eyes-5b-funding-round.htm)
- [Freepik → Magnific, $230M ARR](https://insights.munich-startup.de/news/note/freepik-rebrands-to-magnific-230m-arr-video-ai-pivot-bootstrapped) · [Sacra on OpenArt](https://sacra.com/research/openart)
- [AI video API pricing 2026, devtk.ai](https://devtk.ai/en/blog/ai-video-generation-pricing-2026/) · [ofox.ai fal alternatives](https://ofox.ai/blog/fal-ai-alternatives-video-generation-api-2026/) · [buildmvpfast API costs](https://www.buildmvpfast.com/api-costs/ai-video) · [Rangy pricing explainer](https://rangy.ai/blog/ai-video-pricing-explained/)
- [Nano Banana API pricing, benchlm](https://benchlm.ai/media-pricing/nano-banana)
- [Higgsfield Trustpilot](https://uk.trustpilot.com/review/higgsfield.ai?page=8) · [Higgsfield refund help page](https://higgsfield.ai/creator-hub/help-center/refunds-and-cancellations/how-do-i-request-a-refund) · [MindStudio on cancellation complaints](https://www.mindstudio.ai/blog/higgsfield-subscription-cancellation-complaints)
