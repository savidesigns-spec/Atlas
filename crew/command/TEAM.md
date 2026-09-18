# Command — ATLAS

**Tree:** `crew/command`
**Mandate:** cross-team status, the guardrail policy of record, escalation
path to the Founder. ATLAS doesn't do the work of the three operational
teams — it holds the picture of what all of them are doing and flags what
needs the Founder's call.

## Roster

| Agent | Role | Status |
|---|---|---|
| ATLAS | Commander, Mission Control | proposed — not yet running as a standing process; this session performs ATLAS's function manually (see below) |

## What ATLAS actually is right now

There is no standing "ATLAS" process — the scheduling gap (see
"Escalations" below) means nothing runs unattended on this account yet.
Until that changes, ATLAS's function is performed by whichever
session the Founder is talking to: read this tree plus the three team
trees, reconcile status, surface what's blocked, and route decisions back
here. Treat this file as ATLAS's memory, not ATLAS's runtime.

## The guardrail (policy of record)

This is the canonical copy — `crew/README.md` on the integration branch
carries a summary, this is the source of truth:

> Crew members get standing (no-ask) permission only for actions that
> cannot write to, publish on, or spend against Hglif3.com. Anything that
> publishes content, changes store data, or touches an ad account requires
> an explicit spend/action limit set by the Founder before it runs
> unattended.

Decided 2026-09-18. Changing this requires the Founder's explicit sign-off,
recorded in the decision log below — not a unilateral edit by any agent.

## Cross-team status (as of 2026-09-18)

- **team-ops**: PULSE live, read-only, on-demand. FORGE and CIPHER not built.
- **team-revenue**: nothing built yet. APEX, VAULT, ANCHOR all proposed.
- **team-growth**: nothing built yet. BEACON blocked on ad-account access;
  SCOUT and HORIZON proposed.

## Escalations open to the Founder

1. **Scheduling**: this org's plan blocks connector-bound Routines — needs
   an account-settings check or a decision to build a directly-credentialed
   backend instead. See `crew/README.md` "Known platform gap."
2. **Data access**: no revenue/traffic/ad-spend data reachable yet, which
   blocks BEACON's actual mandate and limits PULSE to content/catalog only.
   Founder decided 2026-09-18 to proceed without it for now — revisit when
   ready.

## Decision log

- **2026-09-18** — Founder: build real standing agents (not just
  in-chat), starting with PULSE, read-only first. Guardrail: crew gets
  standing permission only for actions that can't write/publish/spend;
  everything else needs an explicit limit set first.
- **2026-09-18** — Founder: proceed without deeper analytics/ad-account
  access for now; PULSE runs on catalog/content data only.
- **2026-09-18** — Split crew into 4 trees (this one plus team-revenue,
  team-growth, team-ops) so each team's roster and knowledge can evolve
  independently.
