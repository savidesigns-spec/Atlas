#!/usr/bin/env python3
"""Unit economics for the video broker. Reads pricing.json, prints Markdown.

Usage: python3 economics.py [path/to/pricing.json]

Three questions it answers:
  1. What does each generation cost the user, in credits and dollars?
  2. What gross margin does each plan make at a given utilization?
  3. What happens if we copy Higgsfield's prices and hand out 5x the output?
"""
import json
import math
import sys
from pathlib import Path


def load(path):
    return json.loads(Path(path).read_text())


def credits_for(wholesale_usd, cfg, saver=False):
    price = wholesale_usd * cfg["default_markup"]
    if saver:
        price *= cfg["saver_queue_discount"]
    return math.ceil(price / cfg["credit_face_value_usd"])


def stripe_fee(price, cfg):
    return 0 if price == 0 else price * cfg["stripe_pct"] + cfg["stripe_fixed_usd"]


def blended_cost_per_credit(cfg):
    """Wholesale dollars we pay per credit the user burns, under the usage mix."""
    mix = {k: v for k, v in cfg["assumptions"]["usage_mix"].items() if not k.startswith("_")}
    assert abs(sum(mix.values()) - 1) < 1e-9, "usage_mix must sum to 1"
    total = 0.0
    for key, share in mix.items():
        w = cfg["wholesale"][key]["usd"]
        total += share * w / credits_for(w, cfg)
    return total


def per_output_table(cfg):
    plans = {k: v for k, v in cfg["plans"].items() if not k.startswith("_") and v["price_usd"]}
    pro = plans["pro"]
    rate = pro["price_usd"] / pro["credits"]
    hf = cfg["higgsfield_reference"]
    hf_rate = hf["plus_annual"]["price_usd"] / hf["plus_annual"]["credits"]
    yield_ = hf["advertised_yield_per_1000_credits"]
    hf_price = {
        "kling_3_pro_5s": 1000 / yield_["kling_3_videos"] * hf_rate,
        "nano_banana_pro_2k": 1000 / yield_["nano_banana_pro_images"] * hf_rate,
    }
    rows = ["| Output | Wholesale | Our credits | Our price (Pro plan) | Saver queue | Higgsfield Plus |",
            "|---|---:|---:|---:|---:|---:|"]
    for key, item in cfg["wholesale"].items():
        if key.startswith("_"):
            continue
        c = credits_for(item["usd"], cfg)
        s = credits_for(item["usd"], cfg, saver=True)
        hf_cell = f"${hf_price[key]:.3f}" if key in hf_price else "—"
        rows.append(f"| {item['label']} | ${item['usd']:.3f} | {c} | ${c * rate:.3f} | "
                    f"{s} cr · ${s * rate:.3f} | {hf_cell} |")
    return "\n".join(rows)


def plan_margin_table(cfg):
    cpc = blended_cost_per_credit(cfg)
    utils = cfg["assumptions"]["utilization"]
    head = "| Plan | Price | Credits | " + " | ".join(f"GM @ {int(u * 100)}% used" for u in utils) + " |"
    rows = [head, "|---|---:|---:|" + "---:|" * len(utils)]
    for name, p in cfg["plans"].items():
        if name.startswith("_"):
            continue
        cells = []
        for u in utils:
            cost = p["credits"] * u * cpc + cfg["infra_cost_per_sub_usd"]
            net = p["price_usd"] - stripe_fee(p["price_usd"], cfg) - cost
            if p["price_usd"]:
                cells.append(f"{net / p['price_usd'] * 100:.0f}%")
            else:
                cells.append(f"-${-net:.2f}/user")
        rows.append(f"| {name} | ${p['price_usd']} | {p['credits']:,} | " + " | ".join(cells) + " |")
    for name, t in cfg["topups"].items():
        if name.startswith("_"):
            continue
        cost = t["credits"] * cpc
        net = t["price_usd"] - stripe_fee(t["price_usd"], cfg) - cost
        rows.append(f"| top-up {t['credits']:,} | ${t['price_usd']} | {t['credits']:,} | "
                    + " | ".join([f"{net / t['price_usd'] * 100:.0f}%"] * len(utils)) + " |")
    return cpc, "\n".join(rows)


def five_x_scenario(cfg):
    """Higgsfield's Plus price, 5x its advertised Kling 3.0 yield, paid at wholesale."""
    hf = cfg["higgsfield_reference"]
    price = hf["plus_annual"]["price_usd"]
    videos = hf["advertised_yield_per_1000_credits"]["kling_3_videos"] * 5
    w = cfg["wholesale"]["kling_3_pro_5s"]["usd"]
    rows = ["| Share of allowance used | Videos | Our wholesale bill | Revenue | Profit per user/mo |",
            "|---:|---:|---:|---:|---:|"]
    for u in (0.1, 0.25, 0.5, 1.0):
        n = videos * u
        cost = n * w
        rev = price - stripe_fee(price, cfg)
        rows.append(f"| {int(u * 100)}% | {n:,.0f} | ${cost:,.2f} | ${rev:.2f} | ${rev - cost:,.2f} |")
    breakeven = (price - stripe_fee(price, cfg)) / (videos * w)
    return "\n".join(rows), breakeven


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).with_name("pricing.json")
    cfg = load(path)
    print("## 1. Price per output\n")
    print(per_output_table(cfg))
    cpc, margins = plan_margin_table(cfg)
    print(f"\n## 2. Plan gross margin (blended wholesale ${cpc:.5f}/credit)\n")
    print(margins)
    table, be = five_x_scenario(cfg)
    print("\n## 3. \"Higgsfield price, 5x the output\" on Kling 3.0\n")
    print(table)
    print(f"\nBreak-even: users can touch only {be * 100:.1f}% of the allowance before every sub loses money.")


if __name__ == "__main__":
    main()
