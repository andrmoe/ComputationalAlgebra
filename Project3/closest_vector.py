import numpy as np
from Project3.gram_schmidt import gram_schmidt_basis


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


def closest_vector_search_bounds(i: int, x: np.ndarray, B: np.ndarray, r: np.ndarray[np.float64], A: float) -> np.ndarray:
    if i == x.shape[0] - 1:
        return np.array((0.0, np.sqrt(A/B[x.shape[0] - 1])))
    M1 = np.sqrt((A - B[i+1:].dot(x[i+1:]**2))/B[i])
    M2 = r[i, i + 1:].dot(x[i + 1:])

    return np.array((-M1 - M2, M1 - M2))


def closest_vector_enumeration(basis: np.ndarray, w: np.ndarray) -> np.ndarray:
    bstar, r = gram_schmidt_basis(basis)
    y = np.linalg.solve(bstar, w)
    A = np.linalg.norm(basis[0] - w)**2
    x = np.zeros(w.shape)



    def sub_search(i: int, ):
        pass

