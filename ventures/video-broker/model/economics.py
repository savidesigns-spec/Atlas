#!/usr/bin/env python3
"""Unit economics and the always-profit rule for the video broker.

Usage:
  python3 economics.py            # print the Markdown report
  python3 economics.py --check    # exit 1 if any price breaks profit_rule

The worst case assumes every credit a user can get (plan, bonus pack, founder
kickback, referral payout) is spent at the lowest-markup cost per credit. Saver
queue jobs earn half and cost half, so they don't change the ratio, as long as
saver runs only on providers with a real batch discount (profit_rule enforces that
in the router, not here).
"""
import json
import math
import sys
from pathlib import Path


def load(path):
    return json.loads(Path(path).read_text())


def items(d):
    return {k: v for k, v in d.items() if not k.startswith("_")}


def credits_for(wholesale_usd, cfg, saver=False):
    price = wholesale_usd * cfg["default_markup"]
    if saver:
        price *= cfg["saver_queue_discount"]
    return math.ceil(price / cfg["credit_face_value_usd"])


def stripe_fee(price, cfg):
    return 0 if price <= 0 else price * cfg["stripe_pct"] + cfg["stripe_fixed_usd"]


def worst_cost_per_credit(cfg):
    # credits_for rounds up, so real cost per credit is never above face / markup.
    return cfg["credit_face_value_usd"] / cfg["default_markup"]


def max_kickback_pct(cfg):
    return max(s["pct_of_last_month_spend"] for s in cfg["founders"]["kickback_schedule"])


def referral_payout(plan, cfg):
    r = cfg["referrals"]
    return min(plan["credits"] * r["pct_of_referee_plan_credits"], r["cap_credits_per_referee_month"])


def margin(price, credits, infra, cfg):
    cost = credits * worst_cost_per_credit(cfg) + infra + stripe_fee(price, cfg)
    return (price - cost) / price


def plan_variants(cfg):
    """Yield (label, price, worst-case credits, typical credits, infra)."""
    util = cfg["profit_rule"]["typical_utilization"]
    kick = max_kickback_pct(cfg)
    for name, p in items(cfg["plans"]).items():
        base = p["credits"] + p["bonus_credits"]
        ref = referral_payout(p, cfg)
        worst = base + ref
        yield f"{name} monthly", p["price_usd"], worst, base * util, p["infra_usd"]
        off = cfg["annual"]["discount"][name]
        if off:
            yield f"{name} annual (−{off * 100:.0f}%)", round(p["price_usd"] * (1 - off), 2), worst, base * util, p["infra_usd"]
        f_price = cfg["founders"]["prices_usd"][name]
        f_worst = base * (1 + kick) + ref
        yield f"{name} founder", f_price, f_worst, base * util * (1 + kick), p["infra_usd"]


def topup_variants(cfg):
    for name, t in items(cfg["topups"]).items():
        yield f"top-up {t['credits']:,}", t["price_usd"], t["credits"]
        yield f"top-up {t['credits']:,} (elite −10%)", round(t["price_usd"] * 0.9, 2), t["credits"]


def profit_check(cfg):
    rule = cfg["profit_rule"]
    rows = ["| Price point | $/mo | Worst-case credits | Worst-case GM | Typical GM | Rule |",
            "|---|---:|---:|---:|---:|---|"]
    failures = []
    for label, price, worst, typical, infra in plan_variants(cfg):
        w = margin(price, worst, infra, cfg)
        t = margin(price, typical, infra, cfg)
        ok = w >= rule["floor_margin_worst_case"]
        flag = "ok" if ok else "**FAIL**"
        if ok and t < rule["target_margin_typical"]:
            flag = "ok · below typical target"
        if not ok:
            failures.append(label)
        rows.append(f"| {label} | ${price:,.2f} | {worst:,.0f} | {w * 100:.0f}% | {t * 100:.0f}% | {flag} |")
    for label, price, credits in topup_variants(cfg):
        w = margin(price, credits, 0, cfg)
        ok = w >= rule["floor_margin_worst_case"]
        if not ok:
            failures.append(label)
        rows.append(f"| {label} | ${price:,.2f} | {credits:,} | {w * 100:.0f}% | {w * 100:.0f}% | {'ok' if ok else '**FAIL**'} |")
    return "\n".join(rows), failures


def cac_table(cfg):
    cpc = worst_cost_per_credit(cfg)
    rows = ["| Test | Loss per user (worst case) | Budget cap | Ends | Kill if |",
            "|---|---:|---:|---|---|"]
    total = 0
    for name, t in items(cfg["cac_tests"]).items():
        loss = t["credits"] * cpc + t["infra_usd"] + stripe_fee(t["price_usd"], cfg) - t["price_usd"]
        total += t["budget_cap_usd"]
        rows.append(f"| {t['what']} | ${loss:,.2f} | ${t['budget_cap_usd']:,} | {t['ends']} | {t['kill_if']} |")
    return "\n".join(rows), total


def per_output_table(cfg):
    pro = cfg["plans"]["starter"]
    rate = pro["price_usd"] / pro["credits"]
    hf = cfg["higgsfield_reference"]
    hf_rate = hf["plus_annual"]["price_usd"] / hf["plus_annual"]["credits"]
    yield_ = hf["advertised_yield_per_1000_credits"]
    hf_price = {
        "kling_3_pro_5s": 1000 / yield_["kling_3_videos"] * hf_rate,
        "nano_banana_pro_2k": 1000 / yield_["nano_banana_pro_images"] * hf_rate,
    }
    rows = ["| Output | Wholesale | Credits | Starter-plan $ | Saver queue | Higgsfield Plus |",
            "|---|---:|---:|---:|---:|---:|"]
    for key, item in items(cfg["wholesale"]).items():
        c = credits_for(item["usd"], cfg)
        s = credits_for(item["usd"], cfg, saver=True)
        hf_cell = f"${hf_price[key]:.3f}" if key in hf_price else "—"
        rows.append(f"| {item['label']} | ${item['usd']:.3f} | {c} | ${c * rate:.3f} | "
                    f"{s} cr · ${s * rate:.3f} | {hf_cell} |")
    return "\n".join(rows)


def revenue_ladder(cfg):
    arpu = cfg["assumptions"]["revenue_ladder_arpu_usd"]
    rows = ["| Annual revenue | Paying subscribers needed | Share of Higgsfield's ~$1B |",
            "|---:|---:|---:|"]
    for arr in (1e6, 10e6, 50e6, 100e6, 250e6):
        rows.append(f"| ${arr / 1e6:,.0f}M | {arr / 12 / arpu:,.0f} | {arr / 1e9 * 100:.1f}% |")
    return arpu, "\n".join(rows)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    path = args[0] if args else Path(__file__).with_name("pricing.json")
    cfg = load(path)
    table, failures = profit_check(cfg)
    if "--check" in sys.argv:
        if failures:
            print("Profit rule FAILED for: " + ", ".join(failures))
            sys.exit(1)
        print("Profit rule holds for every plan, founder price, annual price and top-up.")
        return

    print("## 1. Price per output\n")
    print(per_output_table(cfg))
    rule = cfg["profit_rule"]
    print(f"\n## 2. Profit rule: worst case ≥ {rule['floor_margin_worst_case'] * 100:.0f}% "
          f"(every credit spent, incl. bonus, founder kickback at max, referral payout)\n")
    print(table)
    print("\n" + ("All price points pass." if not failures else "FAILING: " + ", ".join(failures)))
    cac, total = cac_table(cfg)
    print("\n## 3. CAC tests (the only allowed losses)\n")
    print(cac)
    print(f"\nTotal loss exposure, capped: ${total:,}")
    arpu, ladder = revenue_ladder(cfg)
    print(f"\n## 4. Revenue ladder at ${arpu} blended ARPU\n")
    print(ladder)


if __name__ == "__main__":
    main()
