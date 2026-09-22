# Wholesale Deals Program — BEACON + ANCHOR

**Started:** 2026-09-22, on the Founder's direct request.
**Goal:** get HGL into retail stores now. Tapstitch (dropship) fulfills
orders of any size, so the usual reason a small brand can't do wholesale
— no inventory to hold against store orders — doesn't apply here.

## Division of labor

- **BEACON** (`crew/team-growth`) — finds and qualifies retail-store
  leads, distributes the line sheet, runs outreach (email now, SMS once
  connected).
- **ANCHOR** (this tree) — owns wholesale pricing, negotiates terms,
  closes the deal, hands the account to fulfillment.

Both report through this doc; it's the single source of truth for the
program, not split across two files that can drift.

## Pricing rule (as specified 2026-09-22)

> Wholesale price = 35% of retail price, unless that conflicts with
> actual product cost — in which case cost is the floor.

This is a real rule, not yet a runnable one — see Blocker 1 and 2 below.
Once both are resolved, the rule is mechanical: `wholesale = max(retail *
0.35, cost)`, per product, computed fresh each time (retail/cost can
change).

## Blockers found while building this (all confirmed 2026-09-22, not assumed)

### 1. No retail price data reachable

Tried two paths, both dead ends:
- `wp_get_post_full` on a live product (id 24488) — WooCommerce's price
  fields (`_price`, `_regular_price`, `_sale_price`) aren't registered
  with `show_in_rest` on this site, so they're invisible to the connector
  entirely. Confirmed: the meta object came back with only tracking/CSS
  fields, no pricing.
- Public storefront fetch (`https://www.hglif3.com/shop/`, which would
  show real customer-facing prices) — blocked by this environment's
  network egress proxy.

**Net effect: I cannot see a single retail price for any of the 16 live
products right now.** The 35%-of-retail calculation has nothing to
compute from.

### 2. No cost data anywhere

Product cost (COGS) is private financial data that was never connected —
not in the WordPress connector, not mentioned anywhere in this build.
Without it, the "unless that conflicts with cost" floor can't be checked
— which means even if retail prices become available, computing a
wholesale price without also having cost risks pricing below cost on
every wholesale order. **Not guessing at cost. Not shipping a pricing
rule that can silently lose money per unit.**

### 3. No SMS channel connected

Checked the connector registry: Twilio, Infobip, and Inkbox all exist as
installable options, none are connected. Email is real and working
(Gmail, confirmed send + draft tools both available). SMS is not — it's
a new integration decision, not something I can enable myself.

### 4. No prospect list

"Send emails of a line sheet" needs recipients. There's no retailer/buyer
contact list anywhere in this build. Cold-emailing invented or scraped
contacts without a real list and clear targeting isn't something to do
by default — it's both low-quality lead gen and a real compliance
surface (CAN-SPAM/TCPA apply to unsolicited commercial email and SMS).
BEACON's first real job, once this program is unblocked, is building
this list deliberately (candidate boutiques/streetwear retailers,
qualified, not just any address found on the internet) — not skipping
straight to a blast.

## Resolution path (2026-09-22, Founder's answers)

- **Pricing data:** retail price → **Shopify**; cost → **Tapstitch**.
  Checked both: a real Shopify MCP connector exists (`get-product`,
  `search_products`, `list-orders`, etc.) but isn't connected yet — I
  can't self-authorize a new store connector, that needs the Founder to
  connect it via claude.ai the same way Hglif3_WordPress was connected.
  Tapstitch has **no MCP connector in the registry at all** — nothing to
  install. Cost data will need to come from the Founder directly (export,
  screenshot, or pasted per-SKU costs), not an API pull.
- **SMS:** skipped for now. Email-only outreach, via the already-working
  Gmail connector.
- **Prospect list:** Founder has existing retailer contacts and will
  provide them directly — BEACON is not researching/cold-building a list.

## What's built despite the blockers

**Line sheet, draft, pricing pending** — `line-sheet-draft.md` in this
tree. Every live product, real descriptions, real product links. Price
columns explicitly marked pending rather than filled with placeholder
numbers, so nobody mistakes a draft for real pricing.

## Guardrail — this is exactly the "client-facing, financial" case

Per the guardrail's original design (`crew/command/TEAM.md`): anything
client-facing or financial routes through the Founder before it leaves
orbit. Outbound wholesale offers to real retailers are both. **Nothing
here — no email, no SMS, no live wholesale price — goes to a real third
party or onto the live store until the Founder has reviewed it,** even
after the four blockers above are resolved. BEACON and ANCHOR draft and
propose; they don't send or publish unsupervised on this program.

## Decision log

- **2026-09-22** — Program started. Four real blockers found and
  documented rather than worked around (fabricated prices, guessed costs,
  or a built-but-empty SMS integration would each look done without
  being real). Line sheet drafted with real products, no invented prices.
- **2026-09-22, later same day** — Founder resolved three of the four:
  pricing comes from Shopify (retail, connector exists but not yet
  connected) + Tapstitch (cost, no connector exists — manual from
  Founder); SMS skipped for now, email-only; prospect list comes from
  Founder's existing contacts, not BEACON research. Still waiting on:
  Shopify connection, Tapstitch cost figures, and the actual contact list.
