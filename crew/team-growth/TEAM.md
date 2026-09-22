# Team Growth — BEACON, SCOUT, HORIZON

**Tree:** `crew/team-growth`
**Mandate:** demand generation, market intelligence, and finding new
territory HGL can expand into. Everything outward-facing that isn't a
direct storefront transaction.

## Roster

| Agent | Module | Mandate | Status |
|---|---|---|---|
| BEACON | Broadcast Array | Leads, licensing, B2B/wholesale opportunities; holds ad spend, reallocates toward ROI | **split status — see below** |
| SCOUT | Long-Range Sensors | Scans the market — competitors, trends, opportunities | proposed |
| HORIZON | Frontier Lab | Scans past current operations for new territory to expand into | proposed |

## BEACON has two separate mandates — one blocked, one now active

**Ad-spend control (still blocked):** holding ad spend, reallocating it in
real time for ROI, requires live access to Google Ads, TikTok Ads, and
Pinterest Ads (all active on Hglif3.com per `crew/README.md`'s plugin
list) plus a real revenue signal to measure ROI against (blocked for the
same reason APEX/VAULT are — see `crew/team-revenue/TEAM.md`). Building
this before either exists would mean building something that *looks*
like it controls ad spend but can't actually see spend or results —
worse than not building it. **Still not building this part.**

**Wholesale lead generation (2026-09-22, now active):** the Founder asked
for a dedicated deals team — retail store outreach, line sheets, wholesale
pricing. This doesn't depend on ad-platform access at all, so it's a
separate, buildable mandate. BEACON's job in this pairing: find and
qualify retail-store leads, distribute the line sheet, run email (and SMS,
once connected) outreach. **ANCHOR (`crew/team-revenue`) closes what
BEACON opens** — full program spec: `crew/team-revenue/wholesale-program.md`.
This is genuinely a two-tree team (lead gen lives in Growth, deal-closing
and pricing/financial terms live in Revenue) rather than one — same real-world
split as a marketing team handing qualified leads to sales.

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
- **2026-09-22** — Founder asked for a dedicated deals team (find leads,
  send line sheets, close wholesale). Split BEACON's mandate: ad-spend
  control stays blocked (unchanged), wholesale lead-gen is now active and
  paired with ANCHOR on `crew/team-revenue`. Full program spec, pricing
  rule, and the four real blockers found while building it (no retail
  price data, no cost data, no SMS channel, no prospect list) live in
  `crew/team-revenue/wholesale-program.md`.
