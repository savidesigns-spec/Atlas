# Team Ops — FORGE, PULSE, CIPHER

**Tree:** `crew/team-ops`
**Mandate:** keeps the station itself running — content, monitoring,
comms/security. The only team with a live agent so far.

## Roster

| Agent | Module | Mandate | Status |
|---|---|---|---|
| **PULSE** | Life Support | Monitors catalog/content health, reports findings | **live — on-demand, read-only** |
| **FORGE** | Fabrication Bay | Builds product/content output | **live — on-demand, draft-only** |
| CIPHER | Comms & Intelligence | Site security, comms, data integrity | proposed |

## PULSE lives on the integration branch, not here

PULSE's spec (`crew/pulse.md`) and its reports (`docs/reports/pulse-*.md`)
stay on `claude/apogee-station-one-pager-cf1eec` rather than being
duplicated into this tree — it's live and working, and moving working
files has real risk (broken references, lost history) for no benefit.
This file is the pointer: PULSE's entry in the roster above, its
findings summarized in the knowledge log below, but its canonical spec
and report history are on the integration branch.

Any *future* team-ops agent (FORGE, CIPHER) should live natively in this
tree from the start — PULSE only doesn't because it predates the
team split.

## FORGE — live as of 2026-09-18

Full spec: `crew/team-ops/forge.md`. Draft-only, standing permission —
mirrors PULSE's read-only carve-out but for content creation instead of
reporting. First output: a draft blog post addressing PULSE's empty-blog
finding, plus a read (not act) on the two stale draft pages. Confirmed
against the live site's own permission system that draft-post creation is
unprompted while taxonomy writes (new categories) are blocked pending
explicit approval — narrower boundary than originally assumed.

## CIPHER — still not buildable as scoped

"Comms & security" as originally scoped assumes access this connector
doesn't have (no security scanning, no direct comms/email tooling beyond
what's separately connected). Needs re-scoping to what's real before it's
buildable — candidate for a proposal once there's a concrete first job for
it, rather than building to the abstract mandate.

## Decision log

- **2026-09-18** — Team tree created. Decided not to migrate PULSE's
  existing files here to avoid breaking working history; future agents
  build natively in this tree.
- **2026-09-18** — FORGE built: draft-only standing permission. Produced
  its first draft (post id 24580) and a recommendation (not an action) on
  the two stale pages. Category creation attempt blocked by platform
  permissions — logged as a real boundary, not just a policy statement.
