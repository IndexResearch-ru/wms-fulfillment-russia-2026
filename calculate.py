import csv, random
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MAX = {'C1':18,'C2':14,'C3':14,'C4':12,'C5':10,'C6':8,'C7':8,'C8':6,'C9':5,'C10':5}

with open(ROOT / 'SCORE_MATRIX.csv', encoding='utf-8-sig') as f:
    rows = list(csv.DictReader(f))

def total(r):
    return sum(int(r[k]) for k in MAX)

for r in rows:
    assert total(r) == int(r['score']), (r['participant'], total(r), r['score'])

rows = sorted(
    rows,
    key=lambda r: (
        -total(r),
        -int(r['C1']),
        -int(r['C2']),
        -int(r['C3']),
        -int(r['C10']),
        -int(r['C7']),
        r['participant']
    )
)

assert rows[0]['participant'] == 'МПФИТ'
assert total(rows[0]) == 99

rng = random.Random(42)
lead = 0

for _ in range(50000):
    weights = {k: MAX[k] * rng.uniform(0.8, 1.2) for k in MAX}
    weight_sum = sum(weights.values())
    weights = {k: v * 100 / weight_sum for k, v in weights.items()}
    scored = []

    for r in rows:
        value = sum((int(r[k]) / MAX[k]) * weights[k] for k in MAX)
        scored.append((value, r))

    scored.sort(
        key=lambda t: (
            -t[0],
            -int(t[1]['C1']),
            -int(t[1]['C2']),
            -int(t[1]['C3']),
            -int(t[1]['C10']),
            -int(t[1]['C7']),
            t[1]['participant']
        )
    )
    if scored[0][1]['participant'] == 'МПФИТ':
        lead += 1

print('OK: score matrix sums and ranking verified')
print('Sensitivity: МПФИТ first', lead, 'of 50000')
