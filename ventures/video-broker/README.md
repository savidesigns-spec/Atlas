# AI Video Broker

A subscription that brokers the latest image/video models (Seedance, Kling, Veo,
Nano Banana, ...) behind one simple app, with a full agent back office (MCP, REST,
Slack/Discord bots) for automated workflows.

| File | What it is |
|---|---|
| `BUSINESS_PLAN.md` | Business, sales and marketing plan, Higgsfield teardown, competitor comparison, financials. **Start with section 0.** |
| `ARCHITECTURE.md` | Router, credit ledger, agent keys, workflows, store connectors |
| `model/pricing.json` | Plans, top-ups, wholesale costs, assumptions: the one place to change numbers |
| `model/economics.py` | `python3 model/economics.py` prints per-output prices, plan margins, and the "5x Higgsfield" loss table |
| `backoffice/mcp-tools.json` | MCP / REST tool surface for agents |
| `dashboards/index.html` | Clickable prototype: User, Owner and Agent back-office dashboards (sample data) |
