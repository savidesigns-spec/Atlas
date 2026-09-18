# Team Growth — BEACON, SCOUT, HORIZON

**Tree:** `crew/team-growth`
**Mandate:** demand generation, market intelligence, and finding new
territory HGL can expand into. Everything outward-facing that isn't a
direct storefront transaction.

## Roster

| Agent | Module | Mandate | Status |
|---|---|---|---|
| BEACON | Broadcast Array | Leads, licensing, B2B/wholesale opportunities; holds ad spend, reallocates toward ROI | blocked on ad-account access |
| SCOUT | Long-Range Sensors | Scans the market — competitors, trends, opportunities | proposed |
| HORIZON | Frontier Lab | Scans past current operations for new territory to expand into | proposed |

## Blocker: BEACON's actual mandate isn't reachable yet

BEACON's one-pager description — holding ad spend, reallocating it in
real time for ROI — requires live access to Google Ads, TikTok Ads, and
Pinterest Ads (all active on Hglif3.com per `crew/README.md`'s plugin
list) plus a real revenue signal to measure ROI against (blocked for the
same reason APEX/VAULT are — see `crew/team-revenue/TEAM.md`). Building
BEACON before either exists would mean building something that *looks*
like it controls ad spend but can't actually see spend or results —
worse than not building it, because it would misrepresent what's real.
**Do not build BEACON's spend-control logic until at least the ad-platform
API access half of this is resolved.**

## What could be built today, scoped to what's real

- **SCOUT** is the most buildable of the three without new access: market
  scanning is largely open-web research (competitor sites, trend
  sources), which doesn't depend on Hglif3.com's connector gaps at all.
  A reasonable next candidate if the Founder wants a second live agent
  after PULSE.
- **HORIZON** is similarly not blocked by the data gap, but its mandate
  (expansion territory) is speculative/strategic rather than operational
  — better suited to periodic, prompted research than a standing process.

## Decision log

- **2026-09-18** — Team tree created. BEACON explicitly flagged as
  blocked rather than built partially/misleadingly; SCOUT identified as
  the team's most buildable next candidate.
