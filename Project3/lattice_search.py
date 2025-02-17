import numpy as np


def gram_schmidt_basis(basis: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    q, r = np.linalg.qr(basis)
    # Applying diag twice results in a matrix with only the diagonal elements from r
    gs_basis = np.diag(np.diag(r)).dot(q)
    gs_r = np.diag(1/np.diag(r)).dot(r)
    return gs_basis, gs_r


def search_bounds(i: int, a: np.ndarray[np.int64], R: np.ndarray[np.float64], A: float) -> np.ndarray:
    abs_Rii = abs(R[i,i])
    if i == a.shape[0] - 1:
        return np.array((0.0, A/abs_Rii))
    Ai = np.sqrt(A**2 - np.sum(R[i+1:,i+1:].dot(a[i+1:]) ** 2))
    Mi = np.sign(R[i,i])*R[i, i+1:].dot(a[i+1:])

    return np.array((-Mi - Ai, -Mi + Ai))/abs_Rii


def search_smallest_vector(basis: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    # Q is orthonormal and R is upper-triangular
    Q, R = np.linalg.qr(basis)
    base_A = np.linalg.norm(basis[0])
    a = np.zeros(basis.shape[1])
    print(basis)
    print(R)
    print(base_A)
    bounds = search_bounds(basis.shape[1]-1, a, R, base_A)
    print(bounds)
    a[-1] = np.floor(bounds[1])
    print(a)
    print(search_bounds(basis.shape[1] - 2, a, R, base_A))

#search_smallest_vector(np.random.random((4, 4)))
