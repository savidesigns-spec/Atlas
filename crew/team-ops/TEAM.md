# Team Ops — FORGE, PULSE, CIPHER

**Tree:** `crew/team-ops`
**Mandate:** keeps the station itself running — content, monitoring,
comms/security. The only team with a live agent so far.

## Roster

| Agent | Module | Mandate | Status |
|---|---|---|---|
| **PULSE** | Life Support | Monitors catalog/content health, reports findings | **live — on-demand, read-only** |
| FORGE | Fabrication Bay | Builds product/content output | proposed |
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

## FORGE and CIPHER — what's actually buildable

- **FORGE**: content creation is reachable today (the WordPress
  connector has full write access to posts/pages/products), gated by the
  standing guardrail — anything it drafts needs Founder approval to
  publish, same as any other write action. A reasonable next candidate:
  PULSE already found two real jobs for it (the empty blog section, the
  two stale draft pages).
- **CIPHER**: "comms & security" as originally scoped assumes access this
  connector doesn't have (no security scanning, no direct comms/email
  tooling beyond what's separately connected). Needs re-scoping to what's
  real before it's buildable — candidate for a proposal once there's a
  concrete first job for it, rather than building to the abstract mandate.

## Decision log

- **2026-09-18** — Team tree created. Decided not to migrate PULSE's
  existing files here to avoid breaking working history; future agents
  build natively in this tree.
