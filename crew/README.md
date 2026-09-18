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

**Chased down 2026-09-18, confirmed (not a bug on our end):**
`ListConnectors` shows Hglif3 WordPress as `connected: true, enabledInChat: true`
— the connector itself is healthy. But `create_trigger`'s `connectors`
parameter — the thing that would let a scheduled Routine carry that
connector into a cron-fired session — returns a flat
`"the connectors parameter is not available for this organization"`
regardless of self-bind or new-session mode. This is an org/plan-level
feature gate, not something fixable from inside a session.

Two real paths forward, neither of which I can do myself:
1. **Org owner checks claude.ai account/billing settings** for a Routine-connector
   feature flag or plan upgrade that unlocks it.
2. **Build a directly-credentialed backend** (real WooCommerce REST API keys +
   GA4/Search Console/ad-platform API credentials, hosted independently of
   the Claude Code Remote connector system). Bigger lift, but it would solve
   *both* this scheduling gap and the deeper data-access gap above in one
   move, since it wouldn't depend on the MCP connector at all.

Until one of those happens: "real autonomous backend agents" means on-demand
runs in a session that already holds the connector, not unattended scheduled
runs. Every crew member inherits this limit, not just PULSE.

## Team structure

Ten crew members is too many to build one at a time with no organization.
As of 2026-09-18 the crew is split into 3 operational teams plus Mission
Control, each with its own dedicated git worktree (a real branch, not just
a folder) so a team's roster, knowledge, and open work can evolve —
agents added, retired, or handed new tools — without churning the other
teams' history or this integration branch.

| Tree (branch) | Members | Mandate |
|---|---|---|
| `crew/command` | ATLAS | Cross-team status, the guardrail policy of record, escalations |
| `crew/team-revenue` | APEX, VAULT, ANCHOR | Money in, money tracked, deals closed |
| `crew/team-growth` | BEACON, SCOUT, HORIZON | Demand generation, market intel, expansion |
| `crew/team-ops` | FORGE, PULSE, CIPHER | Content, monitoring, comms/security |

Each team worktree holds:
- `TEAM.md` — charter, current roster with status (`active` / `proposed` /
  `retired`), and a decision log of what changed and why.
- `knowledge/` — findings a team's agents accumulate (blockers, site
  quirks, what worked) so the next run — by me or a future session —
  doesn't rediscover them from scratch.
- `proposals/` — the process for adding a new agent to a team or retiring
  one. Nothing here spawns or deletes an agent by itself; a proposal is a
  written case (problem, mandate, tools needed, guardrail/autonomy level,
  sunset condition) that becomes real the same way everything else in this
  repo does — reviewed and executed on request, per the standing guardrail
  above. "Self-populating" describes the process being fast and low-friction,
  not unsupervised.

PULSE's existing spec and reports stay put on this integration branch for
now (see `crew/pulse.md`, `docs/reports/`) rather than being migrated —
it's live and working; `crew/team-ops/` points to it instead of duplicating it.
