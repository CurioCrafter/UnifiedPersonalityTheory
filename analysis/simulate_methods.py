#!/usr/bin/env python3
"""Simulations that check our methods. Simulated people are not evidence about real people.

Part 1 asks what H1 and H2 would show if categories were real. Each scale's stable part
is a mix of a two-group category and continuous variation, and `share` is the part of
stable variance that comes from the category. Retest correlation stays fixed at R.

Part 2 relaxes H2's assumption that the four scales are independent.

Usage: python simulate_methods.py     Standard library only, no data needed.
"""
import math
import random

from h1_bimodality import bimodality_coefficient, count_modes, verdict
from h2_type_stability import same_letter

R = 0.835  # midpoint of the reported retest range, see HYPOTHESES.md
N = 20_000
SD, MEAN = 8, 30  # roughly a 10-item scale scored 10 to 50


def two_tests(share, rng):
    """One person's standardised scores on two occasions."""
    c = math.sqrt(share)
    stable = c * rng.choice((-1, 1)) + math.sqrt(1 - share) * rng.gauss(0, 1)
    return tuple(math.sqrt(R) * stable + math.sqrt(1 - R) * rng.gauss(0, 1) for _ in range(2))


def category_row(share, rng):
    pairs = [two_tests(share, rng) for _ in range(N)]
    kept = sum((a > 0) == (b > 0) for a, b in pairs) / N
    scores = [min(50, max(10, round(MEAN + SD * a))) for a, _ in pairs]
    bc, modes = bimodality_coefficient(scores), count_modes(scores)
    return kept, 1 - kept**4, bc, modes, verdict(bc, modes)


def type_change_with_correlated_scales(rho, rng, n=100_000):
    changed = 0
    for _ in range(n):
        shared = rng.gauss(0, 1)
        for _ in range(4):
            first = math.sqrt(rho) * shared + math.sqrt(1 - rho) * rng.gauss(0, 1)
            second = R * first + math.sqrt(1 - R * R) * rng.gauss(0, 1)
            if (first > 0) != (second > 0):
                changed += 1
                break
    return changed / n


if __name__ == "__main__":
    rng = random.Random(1)
    # With no category the simulation must match the closed form from H2.
    assert abs(category_row(0.0, rng)[0] - same_letter(R)) < 0.01
    # With a pure category, keeping a letter follows from the signal-to-noise ratio.
    z = math.sqrt(R / (1 - R))
    p = 0.5 * (1 + math.erf(z / math.sqrt(2)))
    assert abs(category_row(1.0, rng)[0] - (p * p + (1 - p) ** 2)) < 0.01

    print(f"Part 1: retest correlation {R}, N = {N}")
    print("category share  keeps letter  changes type  bc     modes  H1 verdict")
    for share in (0, 0.25, 0.5, 0.6, 0.7, 0.8, 0.9, 1):
        kept, changed, bc, modes, result = category_row(share, rng)
        print(f"{share:<15} {kept:<13.1%} {changed:<13.1%} {bc:<6.3f} {modes:<6} {result}")

    print("\nPart 2: correlation between scales")
    print("correlation  changes type")
    for rho in (0, 0.2, 0.4):
        print(f"{rho:<12} {type_change_with_correlated_scales(rho, rng):.1%}")
