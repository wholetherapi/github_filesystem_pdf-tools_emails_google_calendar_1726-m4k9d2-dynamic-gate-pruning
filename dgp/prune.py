"""Magnitude-based gate pruning (Dynamic Gate Pruning, Interspeech 2026)."""


def prune_gates(weights, keep_ratio=0.4):
    ordered = sorted(range(len(weights)), key=lambda i: abs(weights[i]), reverse=True)
    keep = set(ordered[: max(1, int(keep_ratio * len(weights)))])
    return [w if i in keep else 0.0 for i, w in enumerate(weights)]
