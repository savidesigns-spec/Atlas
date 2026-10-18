# Koolis — how each item actually pays, by channel

**Researched:** 2026-10-18, per the Founder's explicit ask for due diligence
on payment before featuring/advertising any product. Real web research,
not memory — and flagged honestly where sources disagree, since third-party
affiliate-rate guides conflict with each other constantly. **Reconfirm the
specific number against the program's own current terms before committing
ad spend to a product**, not this doc alone.

## The two channels pay completely differently — this matters for "direct pay"

### Dropship (Shopify Collective items, e.g. the leather weekender bags)

Koolis is the **merchant of record**. It buys at the supplier's cost, sets
its own retail price, and keeps the markup. Payment happens **immediately,
directly, at checkout** — through Shopify's own payment processing (Stripe/
Shopify Payments), same as any normal sale. No third party, no waiting
period, no risk of losing the sale to a tracking failure.

This is the closest thing to what "direct pay for our advertising" is
asking for. If Koolis spends money driving traffic to a dropship item, it
gets paid the moment that traffic converts — full stop.

Tradeoff: Koolis owns the customer relationship and any return/support
load (even with Tapstitch-style fulfillment handling logistics), and
margin is finite — bounded by cost + what Koolis can mark it up, not a
brand's commission schedule.

### Affiliate (link-out items)

Koolis is **not** the merchant. It earns a commission when a referred
visitor buys on the brand's own site, tracked by a cookie within an
attribution window, and gets paid **by the affiliate network** (not the
brand directly) on a periodic schedule — **not at the moment of sale.**

This is real revenue leakage risk for a paid-traffic strategy: if the
cookie expires before purchase, or the visitor's browser blocks tracking,
Koolis gets nothing even if its ad drove the sale. Spending real ad
dollars against affiliate links means betting on attribution working,
not a guaranteed payout.

## What the research actually found, by program

| Program | Commission | Cookie window | Who pays, how often | Confidence |
|---|---|---|---|---|
| **Amazon Associates** | 1–10%, varies sharply by category. Luxury beauty ~10%; apparel/watches/handbags ~4%; home/furniture/sports ~3%; electronics/TVs as low as 1–2.5%. | Not confirmed in this research (commonly cited elsewhere as short, ~24hr) | Amazon directly, monthly, NET-60 typical | Low-medium — third-party tables conflict with each other; verify on Associates Central directly |
| **Direct brand programs via Impact** (e.g. YETI) | ~4–7% per sale | ~30 days | Network (Impact) pays, periodic — set day or $10–50 threshold | Medium — sources roughly agree on the 30-day window, less agreement on exact % |
| **Impact (network, general)** | Varies by merchant, "starting at 3%" | Varies by merchant | Impact, $10 minimum cited | Medium |
| **ShareASale (now part of Awin)** | Varies by merchant | Varies by merchant | 20th of month for prior month, $50 threshold (one source cites $20 for Awin) | Low-medium — conflicting thresholds across sources |
| **CJ Affiliate** | "Roughly 3–50%", merchant-dependent | Varies by merchant | 20th or 28th depending on currency, $50 threshold ($100 for check) | Low-medium |

**Sources:** [Amazon Affiliate Commission Rates By Category 2026](https://azonpress.com/amazon-affiliate-commission-rates/) · [Amazon Associates 2026: 20%+ Earning Categories](https://earnifyhub.com/blog/affiliate/amazon-associates-commission-rates-all-categories) · [YETI Affiliate Program: Commission & Program Details (2026)](https://getlasso.co/affiliate/yeti/) · [YETI Affiliate Program Review 2026](https://commissiondex.com/programs/yeti-coolers/) · [Best Affiliate Networks 2026: Impact vs ShareASale vs CJ](https://alternativeentrepreneur.com/affiliate-marketing/best-affiliate-networks/) · [A Comparative Analysis of Leading Affiliate Marketing Networks](https://www.gisaffiliate.com/a-comparative-analysis-of-leading-affiliate-marketing-networks-shareasale-cj-avantlink-and-impact/)

## What this means for sourcing, concretely

- **Lead with dropship for anything Koolis will actually spend ad money
  promoting.** It's the only model that pays directly and immediately —
  matches the Founder's "we need direct pay" requirement exactly.
- **Use affiliate for high-ticket categories Koolis can't stock itself**
  (the original brief: "high ticket items that are searched frequently")
  — but apply to **direct brand programs through Impact**, not Amazon
  Associates, wherever the category allows. Amazon's rates are
  structurally worse for exactly the expensive, frequently-searched
  categories (electronics, premium goods) this brief is targeting — its
  commission tiers are lowest where ticket price is highest. A durable-
  goods brand's own Impact-hosted program (like YETI's) pays better and
  has a longer cookie window.
- **Before featuring any affiliate item in paid advertising**, confirm
  its specific program's real commission rate and cookie window directly
  — this table is a starting map, not a number to build a budget on.

## Decision log

- **2026-10-18** — Researched real payment mechanics per the Founder's
  explicit request, rather than assuming affiliate commissions work like
  dropship margin. Found and flagged that affiliate programs don't pay
  directly/immediately, which matters for paid-advertising ROI — dropship
  is the model that actually satisfies "direct pay." Recommended Impact-
  hosted direct brand programs over Amazon Associates for high-ticket
  affiliate categories specifically because Amazon's rates are worst
  where this brief's "high ticket" target sits.
