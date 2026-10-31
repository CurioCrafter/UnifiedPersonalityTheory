#!/usr/bin/env python3
"""H2: can score reliability alone explain how often people change type? See HYPOTHESES.md.

Model: each scale is a continuous, normally distributed score, cut at its median, with
retest correlation r. Nobody's underlying trait changes. For that case a person lands on
the same side of the cut twice with probability 1/2 + asin(r)/pi. Scales are treated as
independent, so whole-type stability is the product over the four scales.

Usage: python h2_type_stability.py     Standard library only, no data needed.
"""
import math
import random

# Retest correlations for (E-I, S-N, T-F, J-P), as reported in research/01-psychometrics.md.
SCENARIOS = {
    "low end of publisher manual range (all .81)": (0.81, 0.81, 0.81, 0.81),
    "high end of publisher manual range (all .86)": (0.86, 0.86, 0.86, 0.86),
    "pooled review, midpoint (all .835)": (0.835, 0.835, 0.835, 0.835),
    "weak T-F (.75, .75, .61, .75)": (0.75, 0.75, 0.61, 0.75),
}


def same_letter(r):
    return 0.5 + math.asin(r) / math.pi


def same_type(rs):
    return math.prod(same_letter(r) for r in rs)


def simulate(rs, n=200_000, seed=1):
    """Monte Carlo version of the same model, used only to check the formula."""
    rng = random.Random(seed)
    kept = 0
    for _ in range(n):
        for r in rs:
            first = rng.gauss(0, 1)
            second = r * first + math.sqrt(1 - r * r) * rng.gauss(0, 1)
            if (first > 0) != (second > 0):
                break
        else:
            kept += 1
    return kept / n


if __name__ == "__main__":
    for rs in SCENARIOS.values():
        assert abs(simulate(rs) - same_type(rs)) < 0.005, rs
    print("scenario                                        same letter  changes type")
    for name, rs in SCENARIOS.items():
        letters = sum(same_letter(r) for r in rs) / 4
        print(f"{name:<47} {letters:>10.1%}  {1 - same_type(rs):>12.1%}")
