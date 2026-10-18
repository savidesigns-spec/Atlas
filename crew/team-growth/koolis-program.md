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

**Update, 2026-10-18:** the store situation changed entirely since the
note below was written. The Founder connected a *different* Shopify
store — name is now literally **"KOOLIS"**, domain
`tq6geq-yd.myshopify.com`, plan **Basic** (paid, not trial). This is a
different store than "My Store 2" (different domain entirely), not a
rename of it.

**Catalog check, 2026-10-18 — not ready, flagging before anything goes
live:** 33 products exist, but almost none of them pass the quality/
brand-fit rule above:
- Most are unrelated dropship-sample items — soy candles, a $1,102
  hammered-copper kitchen sink, a chandelier, diecast toy trucks, patio
  furniture, kitchen knife sets. Nothing here was vetted; this reads like
  a dropship app's auto-populated starter catalog, not real Koolis picks.
- Two items (vendor "ODMPOD," likely the POD supplier) match real HGL
  product names at $80 — but both are `ARCHIVED` (not live), so $80 isn't
  confirmed as a real finalized price, just what's sitting in the feed.
- Several generic placeholder products ("T-shirt," "Sweater," "Socks,"
  "Accessories") have no description, negative inventory counts, and one
  is priced at **$0.00** — broken test data, not real listings.

**Built anyway, per the Founder's explicit ask, but held back:** the
abandoned "hgL members" page (id 23789) is now retitled "Koolis" and
redirects to `https://tq6geq-yd.myshopify.com/` (meta-refresh + fallback
link). **Still `draft` status — not published.** Publishing it now would
send real HGL members to a storefront full of candles and kitchen knives,
directly against the quality rule this whole program is built on.
**Recommend: don't publish until the catalog is actually cleaned up** —
archive/delete the unrelated dropship-sample products, fix or remove the
broken $0 placeholders, confirm real pricing on the two legitimate items.

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

1. ~~Store rename + theme~~ — **done**, 2026-10-18 (store is now "KOOLIS,"
   Basic plan).
2. ~~Clean the catalog~~ — **done**, 2026-10-18. All 31 unvetted/broken
   products archived (0 active now). The 2 real ODMPOD items are still
   archived pending price confirmation — not reactivated yet.
3. **Product vetting criteria → real candidates: started.** Sourced real
   dropship candidates via Shopify Collective — see "Sourcing" below.
   Still needs: Founder review + actual import (I can't import myself,
   only surface the shelf), and more categories beyond the one that
   panned out.
4. ~~Affiliate program relationships — research~~ — **done**, 2026-10-18.
   Full payment-mechanics research, by channel and by program:
   `koolis-payment-models.md`. Still needs: actually applying to specific
   programs (Impact account, individual brand applications) once
   categories are picked.
5. **Dropship fulfillment cost** — same cost-data gap as HGL's wholesale
   program (`crew/team-revenue/wholesale-program.md` Blocker 2) — need
   real landed cost per product before setting any markup. Collective
   didn't expose margin % either (see Sourcing below) — this is still
   fully open.
6. ~~Link from the "hgL members" page~~ — **done**, 2026-10-18 (redirect
   built, held in draft pending item 2 above — now unblocked, catalog
   is clean, but still pending item 3's real candidates before it's
   worth publishing).

## Sourcing — 2026-10-18

Searched Shopify's Collective dropship marketplace across three candidate
lanes: premium headphones, leather weekender bags, smart fitness watches.
Applied the quality rule honestly rather than forcing a pick in every
lane:

- **Headphones: discarded.** Real headphones in this lane had zero
  reviews (unverifiable quality); only rated items were low-ticket
  accessories (ear pads, headbands), not real headphone products.
- **Smart watches: discarded.** Cheap generics had no reviews; the one
  high-ticket standout — a "refurbished" Apple Watch Series 11 at
  $1,050.30 — came from an obscure third-party reseller ("Uncle LOL"),
  which is exactly the kind of grey-market/counterfeit risk that could
  damage Koolis's credibility. Not worth the brand risk.
- **Leather weekender bags: strong candidates found.** Durable goods,
  genuinely aligned with the "built to last, not fast fashion" ethos.
  Shelf built for Founder review: **Traveler Weekender Duffle** (Classy
  Leather Bags, $120, 4.4★ / **1,273 reviews** — exceptional trust
  signal), **Roosevelt Buffalo Weekender** ($170, 4.5★/37), **Walker
  Leather Weekender Bag + Free Toiletry** ($130, 4.5★/53).

**Import status:** Shopify's Collective channel app needs to be installed
on the KOOLIS store before these can actually be imported — I surfaced
the shelf but can't install the app or import products myself, that's a
merchant action in the Shopify UI. Margin % wasn't exposed by the tool
either; real margin depends on the retail price the Founder sets once
these are actually in the store.

## Decision log

- **2026-09-22** — Program started. Confirmed the connected Shopify
  store is a fresh trial, not HGL's real catalog. Confirmed store
  renaming isn't API-reachable; confirmed theme staging is possible but
  publishing isn't, and the specific theme-install attempt hit a URL
  fetch error on Shopify's side. Recorded the quality-over-price rule as
  the program's non-negotiable, per the Founder's explicit instruction.
- **2026-10-18** — Founder connected a different, new Shopify store
  (now named "KOOLIS," Basic plan — store rename/plan upgrade resolved
  on its own). Audited its 33-product catalog against the quality rule:
  31 don't pass (unrelated dropship-sample junk + broken $0 placeholders),
  2 real HGL-matching items exist but are archived with unconfirmed
  pricing. Built the redirect from the "hgL members" page to this store
  per the Founder's direct request, but held it in `draft` rather than
  publish it — sending real members to this catalog right now would
  directly contradict the quality rule. Recommended a catalog cleanup
  pass before publishing.
- **2026-10-18, later same day** — Founder: clean the catalog, replace
  with vetted high-margin/high-commission picks, and do real due
  diligence on how Koolis gets paid per item before advertising it.
  Archived all 31 junk/broken products (0 active unvetted items remain).
  Sourced real dropship candidates via Shopify Collective — found strong
  ones in leather weekender bags, explicitly discarded headphones and
  smart watches rather than force weak picks (no-reviews generics, and
  one real find — a refurbished Apple Watch — carried real grey-market
  brand risk). Completed real payment-mechanics research across Amazon
  Associates, Impact, ShareASale/Awin, and CJ Affiliate, plus a direct
  brand program (YETI) as a model case — see `koolis-payment-models.md`.
  Key finding: dropship pays directly/immediately (matches the Founder's
  "direct pay" requirement exactly), affiliate pays on a delay through a
  third-party network and carries real attribution/cookie-window risk —
  recommended leading with dropship for anything Koolis spends ad money
  promoting.
