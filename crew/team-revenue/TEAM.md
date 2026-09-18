# Team Revenue — APEX, VAULT, ANCHOR

**Tree:** `crew/team-revenue`
**Mandate:** money in, money tracked, deals closed. Everything that
touches the storefront, the store's financial position, and B2B/wholesale
contracts.

## Roster

| Agent | Module | Mandate | Status |
|---|---|---|---|
| APEX | Docking Bay · Commerce | Storefront, orders, live sales data | proposed |
| VAULT | The Vault · Treasury & Inventory | Cash position, stock levels, financial integrity | proposed |
| ANCHOR | Docking Clamp | Negotiates and closes B2B/wholesale/licensing deals | proposed |

None of the three are built yet — see the blocker below before proposing
implementation work for APEX or VAULT specifically.

## Blocker: no order/revenue data source

Per `crew/command/knowledge/platform-limits.md`: the WordPress connector
exposes product *catalog* (titles, status, dates) but not orders, revenue,
or inventory levels — those live in WooCommerce's own tables and aren't
REST-exposed through what's currently connected. **APEX and VAULT cannot
do their actual jobs (live sales data, cash position) until that's fixed.**
ANCHOR is less blocked — deal-closing is more judgment/negotiation than
data-pull — but has no CRM or contract system connected yet either.

## What could be built today, scoped to what's real

- A catalog-hygiene pass (product descriptions, pricing consistency,
  category coverage) is content-level and already reachable — closer to
  FORGE's territory than APEX's real mandate, but worth noting as a
  stopgap if the Founder wants visible progress here before the data
  gap closes.

## Decision log

- **2026-09-18** — Team tree created. No agents built yet; roster is a
  placeholder pending the order/revenue data-access decision recorded in
  `crew/command/TEAM.md`.
