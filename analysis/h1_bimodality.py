#!/usr/bin/env python3
"""H1: are the traits that MBTI scales overlap with bimodal? See HYPOTHESES.md.

Usage:
  python h1_bimodality.py --self-check
  python h1_bimodality.py path/to/data.csv     # BIG5.zip from openpsychometrics.org/_rawdata/

Standard library only. The data is not stored in this repo; its licence is not stated.
"""
import csv
import random
import statistics
import sys

# Keys from the IPIP 50-item page, in the data's item order. -1 means reverse-scored.
# N is scored towards Neuroticism, the opposite of the page's Emotional Stability.
KEYS = {
    "E": [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],
    "N": [1, -1, 1, -1, 1, 1, 1, 1, 1, 1],
    "A": [-1, 1, -1, 1, -1, 1, -1, 1, 1, 1],
    "C": [1, -1, 1, -1, 1, -1, 1, -1, 1, 1],
    "O": [1, -1, 1, -1, 1, -1, 1, 1, 1, 1],
}
BC_THRESHOLD = 5 / 9  # value for a uniform distribution; higher suggests bimodality
MIN_PROMINENCE = 0.05  # a mode must rise this share of the highest peak above its valleys


def bimodality_coefficient(xs):
    n = len(xs)
    mean = statistics.fmean(xs)
    sd = statistics.pstdev(xs, mean)
    g1 = sum(((x - mean) / sd) ** 3 for x in xs) / n
    g2 = sum(((x - mean) / sd) ** 4 for x in xs) / n - 3
    return (g1**2 + 1) / (g2 + 3 * (n - 1) ** 2 / ((n - 2) * (n - 3)))


def count_modes(xs):
    """Modes of the 3-point smoothed histogram of integer scores."""
    lo, hi = min(xs), max(xs)
    counts = [0] * (hi - lo + 3)  # zero pad at both ends
    for x in xs:
        counts[x - lo + 1] += 1
    smooth = [
        (counts[max(i - 1, 0)] + counts[i] + counts[min(i + 1, len(counts) - 1)]) / 3
        for i in range(len(counts))
    ]
    floor = MIN_PROMINENCE * max(smooth)
    modes, peak, valley, climbing = 0, 0.0, 0.0, True
    for v in smooth:
        if climbing:
            peak = max(peak, v)
            if peak - v >= floor and peak - valley >= floor:
                modes += 1  # the climb ended in a real drop
                valley, climbing = v, False
        else:
            valley = min(valley, v)
            if v - valley >= floor:
                peak, climbing = v, True
    return modes


def verdict(bc, modes):
    if bc <= BC_THRESHOLD and modes == 1:
        return "continuous"
    if bc > BC_THRESHOLD and modes >= 2:
        return "two-peaked"
    return "mixed"


def score(rows):
    """Sum keyed answers per trait. Rows with a blank or 0 answer on a trait are dropped."""
    scores, flipped = {}, []
    for trait, key in KEYS.items():
        cols = [f"{trait}{i + 1}" for i in range(10)]
        keyed = []
        for row in rows:
            answers = [row[c] for c in cols]
            if all(a in "12345" and a for a in answers):
                keyed.append([int(a) if k > 0 else 6 - int(a) for a, k in zip(answers, key)])
        scores[trait] = [sum(k) for k in keyed]
        # A wrong key shows up as a negative correlation with the rest of the scale.
        for i, col in enumerate(cols):
            item = [k[i] for k in keyed]
            rest = [sum(k) - k[i] for k in keyed]
            if statistics.correlation(item, rest) <= 0:
                flipped.append(col)
    return scores, flipped


def analyse(path):
    with open(path, newline="", encoding="utf-8") as f:
        delimiter = "\t" if "\t" in f.readline() else ","
        f.seek(0)
        rows = list(csv.DictReader(f, delimiter=delimiter))
    scores, flipped = score(rows)
    if flipped:
        sys.exit(f"Keys disagree with the data, not reporting results: {flipped}")
    print("trait  n       bc     modes  verdict")
    for trait, xs in scores.items():
        bc, modes = bimodality_coefficient(xs), count_modes(xs)
        print(f"{trait:<6} {len(xs):<7} {bc:.3f}  {modes:<6} {verdict(bc, modes)}")


def self_check():
    rng = random.Random(1)
    one = [round(rng.gauss(30, 6)) for _ in range(20000)]
    two = [round(rng.gauss(rng.choice((20, 40)), 3)) for _ in range(20000)]
    assert verdict(bimodality_coefficient(one), count_modes(one)) == "continuous"
    assert verdict(bimodality_coefficient(two), count_modes(two)) == "two-peaked"

    # A wrongly keyed scale must be caught.
    rows = []
    for _ in range(2000):
        latent = rng.gauss(0, 1)
        row = {}
        for trait, key in KEYS.items():
            for i, k in enumerate(key):
                value = min(5, max(1, round(3 + k * latent + rng.gauss(0, 0.8))))
                row[f"{trait}{i + 1}"] = str(value)
        rows.append(row)
    assert score(rows)[1] == []
    for row in rows:
        row["E1"] = str(6 - int(row["E1"]))
    assert score(rows)[1] == ["E1"]
    print("self-check passed")


if __name__ == "__main__":
    if sys.argv[1:] == ["--self-check"]:
        self_check()
    elif len(sys.argv) == 2:
        analyse(sys.argv[1])
    else:
        sys.exit(__doc__)
