"""Metrics for comparing ideal probability distributions and sampled counts."""

from collections.abc import Mapping


def counts_to_probabilities(counts: Mapping[str, int]) -> dict[str, float]:
    """Normalize non-negative measurement counts into probabilities."""
    if not counts:
        raise ValueError("counts must not be empty")
    if any(not isinstance(value, int) or value < 0 for value in counts.values()):
        raise ValueError("counts must contain non-negative integer values")
    total = sum(counts.values())
    if total <= 0:
        raise ValueError("counts must have a positive total")
    return {key: value / total for key, value in counts.items()}


def total_variation_distance(first: Mapping[str, float], second: Mapping[str, float]) -> float:
    """Return TVD = 0.5 * sum_x |P(x) - Q(x)| over the union of keys.

    Inputs should be probability distributions. The function validates finite,
    non-negative values and checks that each distribution sums to one.
    """
    if not first or not second:
        raise ValueError("distributions must not be empty")
    for distribution in (first, second):
        if any(value < 0 or value > 1 for value in distribution.values()):
            raise ValueError("probabilities must be in [0, 1]")
        if abs(sum(distribution.values()) - 1.0) > 1e-8:
            raise ValueError("each distribution must sum to 1")
    keys = set(first) | set(second)
    return 0.5 * sum(abs(first.get(key, 0.0) - second.get(key, 0.0)) for key in keys)
