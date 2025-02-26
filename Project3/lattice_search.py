import numpy as np
from gram_schmidt import gram_schmidt_basis
from generic_search import generic_enumeration
from typing import Iterable


def search_smallest_vector(basis: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    bstar, r = gram_schmidt_basis(basis)
    bstar_lengths = np.linalg.norm(bstar, axis=0)

    def search_range(i: int, a: [int], A: float) -> Iterable[int]:
        a = np.array(a)
        if i == a.shape[0] - 1:
            return range(0, int(np.ceil(A / bstar_lengths[i])))
        # TODO: Fix omitted ||b*||^2
        radix = A**2 - np.sum(
            r[i + 1 :, i + 1 :].dot(a[i + 1 :] * bstar_lengths[i + 1 :]) ** 2
        )
        if radix < 0:
            return range(0)
        Ai = np.sqrt(radix) / bstar_lengths[i]
        Mi = r[i, i + 1 :].dot(a[i + 1 :])

        return range(int(np.ceil(-Mi - Ai)), int(np.ceil(-Mi + Ai)))

    def score_func(a: [int]) -> float:
        if np.allclose(a, 0):
            return float(np.inf)
        return float(np.linalg.norm(basis.dot(a)))

    shortest_a, _ = generic_enumeration(
        basis.shape[1],
        0,
        search_range,
        score_func,
        min([np.linalg.norm(b) for b in basis.T]),
    )
    shortest_a = np.array(shortest_a)
    return basis.dot(shortest_a), shortest_a
