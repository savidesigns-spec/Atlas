# Website design: v0.1

`index.html` (home) and `founders.html` are designed. Shared tokens and components live
in `styles.css`. Both are static files you can open in a browser, with light and dark mode
and widths down to 360px. This doc is the system they're built on and the plan for the
remaining pages.

## Direction
**"The honest studio."** A warm paper/ink palette with one hot accent, for a site that
reads like a premium tool rather than a neon AI toy. That deliberately contrasts with
Higgsfield's black-and-lime hype look.

The signature element is the **receipt**: a torn-edge, monospace card showing exactly
what a job cost. It appears in the hero, in the product and in marketing creatives. It
*is* the brand promise.

## Tokens
| Token | Light | Dark | Use |
|---|---|---|---|
| `--bg` | `#f5f2ec` | `#0e0d0b` | Page |
| `--bg-2` | `#ebe6dc` | `#161411` | Alternating sections |
| `--panel` | `#fffdf9` | `#1b1915` | Cards |
| `--ink` | `#15130f` | `#f3efe7` | Text, inverted sections |
| `--muted` | `#625c52` | `#a39b8e` | Secondary text |
| `--accent` | `#e0561f` | `#ff7a45` | CTAs, founder program, highlights |
| `--cool` | `#3554d1` | `#8ea4ff` | Secondary accent (logo, charts) |
| `--good` | `#2f7d3b` | `#6cc27a` | Refunds, success |

**Type:**
- **Inter Tight** for UI and headings
- **Instrument Serif italic** for the one emotional phrase per headline
- **JetBrains Mono** for receipts, prices, eyebrows and code

Radius is 14px on cards and pills on buttons. Use one primary CTA per view.

## Voice
- Plain, specific, a bit dry.
- Say the number ("6,000 credits ≈ 66 Kling clips"), never "unlimited."
- Never claim "cheapest." Claim *transparent, automated, no expiring credits*.
- Compare against "typical platforms" by behavior. Don't name Higgsfield on the site
  until legal has reviewed the comparison claims.

## Sitemap
| Page | Status | Notes |
|---|---|---|
| Home `/` | **designed** | `index.html` |
| Pricing `/pricing` | in home | Split out with a full feature matrix + top-up calculator |
| Founders `/founders` | **designed** | `founders.html`: seat counter, autoplay showcase wall, kickback calculator, rules, sticky CTA |
| Models `/models` | next | Live credit price per model from `pricing.json`, provider terms links |
| Automate `/automate` | next | Template gallery: store ads, UGC, weekly content |
| For agents `/agents` | next | MCP connector setup, REST docs, spend-cap explainer |
| Compare `/compare` | later | SEO pages: "Higgsfield alternative", "Seedance 2.0 price", … |
| Sign up / Sign in | later | $1 trial checkout (Stripe), card required |
| App `/app` | prototype | `../dashboards/index.html` (User / Owner / Agents) |

## Rules before launch
- The **founder seat counter must be live** from the database. A hard-coded "8,996 left"
  is a fake-scarcity dark pattern and an FTC risk.
- The prices in the page script mirror `model/pricing.json`. Change prices there first,
  run `python3 model/economics.py --check`, then update the site.
- Comparison-table claims need a dated source. Keep the footnote.
- Use real generated outputs in the hero frames (the gradients are placeholders). Make
  them with the product itself.
- Founders copy must stay honest about value. At full use and the top 20% rate, kickbacks are worth about three-quarters of the founder premium; the price lock and perks are the rest. Never say "paid back" or imply cash.
- Video loops follow the loading rules in `../infra/infrastructure-plan.html` §9: poster first, play only on screen, max 3 at once.
