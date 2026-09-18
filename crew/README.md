# Apogee Station — Crew Build

This directory is the working build-out of the Apogee Station crew described in
`docs/apogee-station-one-pager.html`. Each crew member gets a spec file here:
mandate, tools it actually has, what it produces, and its autonomy level.

## Status

| Crew member | Role | Status | Autonomy |
|---|---|---|---|
| ATLAS | Commander, Mission Control | not built | — |
| APEX | Docking Bay · Commerce | not built | — |
| CIPHER | Comms & Intelligence | not built | — |
| VAULT | Treasury & Inventory | not built | — |
| FORGE | Fabrication Bay | not built | — |
| **PULSE** | **Life Support · Analytics** | **live** | **on-demand — read-only** |
| SCOUT | Long-Range Sensors | not built | — |
| BEACON | Broadcast Array · Ad spend | not built | blocked on ad-account access |
| ANCHOR | Docking Clamp · Deal closing | not built | — |
| HORIZON | Frontier Lab | not built | — |

## Standing guardrail

Per the Founder's decision (2026-09-18): crew members get standing (no-ask)
permission only for actions that cannot write to, publish on, or spend
against Hglif3.com. Anything that publishes content, changes store data,
or touches an ad account requires an explicit spend/action limit to be set
by the Founder before it runs unattended. See each crew member's spec for
its current limit (or lack of one).

## Known data gaps (as of 2026-09-18)

The WordPress connector into Hglif3.com (Easy MCP AI plugin) currently
exposes 88 of its 243 tools to this session — core content/catalog CRUD
(posts, pages, products, terms, media, comments, users), but **no
WooCommerce order/revenue data, no GA4, no Search Console, and no ad
platform (Google/TikTok/Pinterest Ads) access.** PULSE's reports below are
built entirely from content/catalog data because of this. Real sales,
traffic, and ad-spend ROI reporting (and any of BEACON's ad-spend mandate)
needs one of:

1. Enabling the missing tool groups in WP Admin → Easy MCP AI → Settings, or
2. Direct API credentials for GA4 / Search Console / the ad platforms.

Decided 2026-09-18: proceed without this for now — PULSE runs on what's
already accessible.

## Known platform gap: no scheduled autonomy yet

This Anthropic org's plan does not support attaching MCP connectors
(including Hglif3_WordPress) to a scheduled Routine/trigger, so a cron-fired
PULSE run would wake up with no access to the site. Until that's available
(or PULSE gets a directly-credentialed data path instead of going through
the WordPress MCP connector), "real autonomous backend agents" in practice
means: on-demand runs in a session that already holds the connector, not
unattended scheduled runs. This applies to every crew member, not just
PULSE — anything built here inherits the same limit until it's resolved.
