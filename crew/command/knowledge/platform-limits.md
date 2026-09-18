# Platform limits — what every team needs to know before proposing an agent

Keep this updated as new limits are discovered. A proposal that assumes
something this file already rules out is a wasted review cycle.

## No connector-bound scheduling (2026-09-18)

`create_trigger`'s `connectors` parameter is rejected outright for this
org: `"the connectors parameter is not available for this organization"`.
Confirmed this isn't a naming or auth issue — `ListConnectors` shows
Hglif3 WordPress as `connected: true, enabledInChat: true` in this very
session. It's a flat plan/org-level feature gate. **Consequence: no crew
member can run on a real unattended schedule with WordPress access right
now, however low-risk.** Any proposal that assumes standing scheduled
autonomy needs one of the two fixes in `crew/README.md` first.

## WordPress connector tool coverage (2026-09-18)

The Hglif3_WordPress MCP connector exposes 88 tools: posts, pages, products
(catalog only — no price/stock meta in the generic CPT schema), media,
comments, menus, terms, users. Confirmed absent: WooCommerce
orders/revenue, GA4, Search Console, any ad platform (Google/TikTok/
Pinterest Ads) despite all of those being active plugins/integrations on
the live site. A proposal for an agent whose mandate is revenue, traffic,
or ad-spend reporting/control needs one of the two data-access fixes in
`crew/README.md` first — it cannot be built on what's currently connected.

## What *is* real and working

Content/catalog read AND write access to Hglif3.com (live, production,
16 published products as of 2026-09-18) via this session's WordPress
connector. Any proposal scoped to content, catalog hygiene, or site
structure can be built today, on-demand, standing-permission rules per
`crew/command/TEAM.md` applying to anything that writes.
