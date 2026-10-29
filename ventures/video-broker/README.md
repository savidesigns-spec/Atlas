# AI Video Broker

A subscription that brokers the latest image/video models (Seedance, Kling, Veo,
Nano Banana, ...) behind one simple app, with a full agent back office (MCP, REST,
Slack/Discord bots) for automated workflows.

| File | What it is |
|---|---|
| `BUSINESS_PLAN.md` | Business, sales and marketing plan, Higgsfield teardown, competitor comparison, financials. **Start with section 0.** |
| `ARCHITECTURE.md` | Router, credit ledger, agent keys, workflows, store connectors |
| `model/pricing.json` | Plans, Founding Member program, top-ups, CAC tests, wholesale costs: the one place to change numbers |
| `model/economics.py` | Prints per-output prices, the profit-rule table, CAC exposure and the $250M revenue ladder. `--check` fails on any price that could lose money (runs in CI: `.github/workflows/profit-rule.yml`) |
| `backoffice/mcp-tools.json` | MCP / REST tool surface for agents |
| `dashboards/index.html` | Clickable prototype: User, Owner and Agent back-office dashboards (sample data) |
| `site/index.html` | Home page design (light/dark, mobile) with pricing, Founders and agents sections |
| `site/DESIGN.md` | Design tokens, voice, sitemap, pre-launch rules |
| `site/founders.html` | Founding Member page: seat counter, showcase wall, kickback calculator |
| `infra/Studio-Infrastructure-Funding-Launch-Plan.pdf` | 16-page plan: customer-funded cash flow, 37-component list, own servers vs managed hosting, staged path, fast-video rules, visual references. Source: `infra/infrastructure-plan.html`; rebuild with `node infra/render_pdf.js` |
