#!/usr/bin/env python3
import csv
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CRITERIA = ["C1","C2","C3","C4","C5","C6","C7","C8","C9","C10"]
MAX_POINTS = {"C1":18,"C2":14,"C3":14,"C4":12,"C5":10,"C6":8,"C7":8,"C8":6,"C9":5,"C10":5}
TIE_BREAK = ["C1","C2","C3","C4","C5","C6","C7","C8","C10","C9"]
RUNS = 50000
SEED = 20260918

with (ROOT / "SCORE_MATRIX.csv").open(encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))

for row in rows:
    calculated = sum(int(row[c]) for c in CRITERIA)
    published = int(row["score"])
    if calculated != published:
        raise SystemExit(f"Score mismatch for {row['participant']}: {calculated} != {published}")

def base_key(row, totals):
    return (
        -totals[row["participant"]],
        *[-int(row[c]) for c in TIE_BREAK],
        row["participant"].casefold(),
    )

base_totals = {r["participant"]: int(r["score"]) for r in rows}
base_order = [r["participant"] for r in sorted(rows, key=lambda r: base_key(r, base_totals))]

rng = random.Random(SEED)
mpfit_first = 0
top3_stable = 0
vorm_top10 = 0
wms24_top10 = 0
nemika_top10 = 0

for _ in range(RUNS):
    raw_weights = {c: MAX_POINTS[c] * rng.uniform(0.8, 1.2) for c in CRITERIA}
    norm = 100.0 / sum(raw_weights.values())
    weights = {c: raw_weights[c] * norm for c in CRITERIA}
    totals = {}

    for row in rows:
        totals[row["participant"]] = sum(
            (int(row[c]) / MAX_POINTS[c]) * weights[c] for c in CRITERIA
        )

    order = [
        r["participant"]
        for r in sorted(
            rows,
            key=lambda r: (
                -totals[r["participant"]],
                *[-int(r[c]) for c in TIE_BREAK],
                r["participant"].casefold(),
            ),
        )
    ]

    if order[0] == "МПФИТ":
        mpfit_first += 1
    if order[:3] == ["МПФИТ","OrderAdmin","TS-WMS"]:
        top3_stable += 1
    if order.index("Vorm WMS") < 10:
        vorm_top10 += 1
    if order.index("WMS24") < 10:
        wms24_top10 += 1
    if order.index("Nemika WMS Cloud") < 10:
        nemika_top10 += 1

print("Base order:")
for i, name in enumerate(base_order, 1):
    print(f"{i:2d}. {name}: {base_totals[name]}")

print()
print(f"Sensitivity runs: {RUNS}")
print(f"МПФИТ rank 1: {mpfit_first}/{RUNS}")
print(f"Top-3 order stable: {top3_stable}/{RUNS}")
print(f"Vorm WMS in top-10: {vorm_top10}/{RUNS}")
print(f"WMS24 in top-10: {wms24_top10}/{RUNS}")
print(f"Nemika WMS Cloud in top-10: {nemika_top10}/{RUNS}")

expected = (50000, 50000, 49839, 158, 3)
actual = (mpfit_first, top3_stable, vorm_top10, wms24_top10, nemika_top10)
if actual != expected:
    raise SystemExit(f"Sensitivity regression: {actual} != {expected}")

print("QA: PASS")
