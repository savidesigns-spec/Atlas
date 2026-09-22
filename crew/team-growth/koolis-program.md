# KOOLIS — HGL Members Benefit (curated dropship + affiliate)

**Started:** 2026-09-22, Founder's direct request.
**Owner:** HORIZON (new-territory mandate — this is HGL's first real
expansion beyond the streetwear line). FORGE builds the member-facing
page once there's real content to put on it.
**What it is:** a curated marketplace for HGL members — quality products
Koolis has vetted so members don't have to. Two revenue paths: items
Koolis dropships itself (through Tapstitch-style fulfillment) for a
markup, and items it links out to as an affiliate.

## The one rule everything else follows

> Quality — great reviews, durability, longevity, brand fit — beats
> price. Never pick a product because it's the cheapest option available;
> pick it because it's genuinely good. (Founder, 2026-09-22.)

This applies identically to dropship picks and affiliate picks. Koolis's
whole value proposition is *"we already did the research so you don't
have to"* — a curation service that would pick the cheap-but-mediocre
option isn't delivering that, it's just another marketplace.

## Vetting criteria (working draft — refine as real candidates come in)

A product qualifies for Koolis if it clears all of:
1. **Reviews** — a real, consistent track record of positive reviews
   across independent sources, not just the seller's own listing.
2. **Durability/longevity** — built to last, not disposable — the
   opposite of fast fashion, matching HGL's own brand stance.
3. **Brand fit** — something an HGL member would expect to see
   recommended by HGL. Quality-of-life, style, lifestyle — not random
   drop-shippable junk that happens to be profitable.
4. **Margin makes sense for the channel** — dropship items need a markup
   that still lands at a fair member price after Tapstitch-style
   fulfillment cost; affiliate items need a legitimate program (no
   picking a worse product because its affiliate commission is bigger).

## Two channels, two mechanics

- **Dropship-for-markup:** Koolis lists the product, fulfillment runs
  through a Tapstitch-style partner (same fulfillment model as HGL's own
  wholesale program — see `crew/team-revenue/wholesale-program.md`), Koolis
  sets the member-facing price above landed cost.
- **Affiliate:** Koolis doesn't hold the product at all — links out,
  earns commission. Needs real affiliate program relationships per
  vendor/category; none are set up yet (see Open items).

## Where this lives, technically

**A Shopify store is now connected to this session** — "My Store 2"
(`ruxcnj-ub.myshopify.com`), a fresh, empty **trial-plan** store (Shopify's
own tool requires this be said plainly: *"Plan: trial — you'll need to
upgrade before you can start selling and unlock full features."*). This
is the intended home for Koolis's storefront.

**What I tried and what actually happened, 2026-09-22:**
- Renaming the store ("My Store 2" → "Koolis"): **not possible via API** —
  confirmed by searching the full Shopify Admin GraphQL mutation schema,
  there is no shop-rename mutation. This is a Shopify Admin setting the
  Founder has to change directly: **Shopify Admin → Settings → General
  → Store details.**
- Installing a theme: theme mutations do exist (`themeCreate`,
  `themePublish`, etc.) and `themeCreate` is *not* blocked by this
  connector's safety rules (unlike `themePublish`, which is blocked
  outright — a theme can be staged but not published through this
  connector). Tried installing Shopify's free "Dawn" theme from its
  public GitHub zip; the mutation ran but Shopify's server couldn't
  fetch that URL ("Src is empty"). Rather than keep guessing at URL
  variants, the simpler and more reliable path is the one built for
  exactly this: **Shopify Admin → Online Store → Themes → Add theme →
  Explore free themes** — one click, no API fragility.

Both of those are two-minute manual steps for the Founder; not worth
more API back-and-forth to force through this connector.

## Open items before anything goes live

1. **Store rename + theme** — Founder action in Shopify Admin (above).
2. **Product vetting criteria → real candidates** — nobody's sourced
   actual products yet. Next step once this doc is confirmed.
3. **Affiliate program relationships** — none set up. Needs research per
   category (which vendors/programs actually pay affiliates and fit the
   quality bar).
4. **Dropship fulfillment cost** — same cost-data gap as HGL's wholesale
   program (`crew/team-revenue/wholesale-program.md` Blocker 2) — need
   real landed cost per product before setting any markup.
5. **Link from the "hgL members" page** — the abandoned stub on
   hglif3.com (page id 23789, flagged by PULSE and FORGE as empty/near-
   empty) is the natural place to announce Koolis to HGL's existing
   audience. FORGE's job once Koolis has real content to point to.

## Decision log

- **2026-09-22** — Program started. Confirmed the connected Shopify
  store is a fresh trial, not HGL's real catalog. Confirmed store
  renaming isn't API-reachable; confirmed theme staging is possible but
  publishing isn't, and the specific theme-install attempt hit a URL
  fetch error on Shopify's side. Recorded the quality-over-price rule as
  the program's non-negotiable, per the Founder's explicit instruction.
