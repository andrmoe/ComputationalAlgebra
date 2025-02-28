import numpy as np
from gram_schmidt import gram_schmidt_basis
from generic_search import generic_enumeration
from typing import Iterable


def rounding(basis: np.ndarray, w: np.ndarray) -> np.ndarray:
    a = np.linalg.solve(basis, w)
    a = np.round(a)
    return basis.dot(a)


def babai_nearest_plane(basis: np.ndarray, w: np.ndarray) -> np.ndarray:
    bstar, _ = gram_schmidt_basis(basis)
    ys = np.zeros(basis.shape)
    for i in range(basis.shape[1] - 1, -1, -1):
        li = w.dot(bstar.T[i]) / bstar.T[i].dot(bstar.T[i])
        ys.T[i] = np.round(li) * basis.T[i]
        w = w - (li - np.round(li)) * bstar.T[i].T - np.round(li) * basis.T[i].T
    return np.sum(ys, axis=1)


def closest_vector_enumeration(basis: np.ndarray, w: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    bstar, r = gram_schmidt_basis(basis)
    bstar_lengths = np.linalg.norm(bstar, axis=0)
    y = np.linalg.solve(bstar, w)
    A = np.min(np.linalg.norm(basis - w, axis=0))

    def search_range(i: int, a: [int], A: float) -> Iterable[int]:
        a = np.array(a)
        if i == len(a) - 1:
            Mi = np.ceil(A / bstar_lengths[i])
            Ni = -y[i]
            return range(int(np.ceil(-Mi-Ni)), int(np.ceil(Mi-Ni)))
        radicand = A**2 - np.sum(
            (
                (r[i + 1 :, i + 1 :].dot(a[i + 1 :]) - y[i + 1 :])
                * bstar_lengths[i + 1 :]
            )
            ** 2
        )
        if radicand < 0:
            return range(0)
        Mi = np.sqrt(radicand) / bstar_lengths[i]
        Ni = r[i, i + 1 :].dot(a[i + 1 :]) - y[i]
        return range(int(np.ceil(-Mi - Ni)), int(np.ceil(Mi - Ni)))

    def score_func(a: [int]) -> float:
        return float(np.linalg.norm(basis.dot(a) - w))

    closest_a, score = generic_enumeration(
        basis.shape[1], 0, search_range, score_func, A
    )
    closest_a = np.array(closest_a)
    return basis.dot(closest_a), closest_a
