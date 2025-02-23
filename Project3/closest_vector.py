import numpy as np
from gram_schmidt import gram_schmidt_basis


def rounding(basis: np.ndarray, w: np.ndarray) -> np.ndarray:
    a = np.linalg.solve(basis, w)
    a = np.round(a)
    return basis.dot(a)


def babai_nearest_plane(basis: np.ndarray, w: np.ndarray) -> np.ndarray:
    bstar, _ = gram_schmidt_basis(basis)
    ys = np.zeros(basis.shape)
    for i in range(basis.shape[1] - 1, -1, -1):
        li = w.dot(bstar.T[i])/bstar.T[i].dot(bstar.T[i])
        ys.T[i] = np.round(li)*basis.T[i]
        w = w - (li - np.round(li)) * bstar.T[i].T - np.round(li) * basis.T[i].T
    return np.sum(ys, axis=1)
