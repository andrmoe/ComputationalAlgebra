import numpy as np
from numpy.linalg import norm
from gram_schmidt import gram_schmidt_basis


def is_size_reduced(r: np.ndarray) -> bool:
    x = r - np.diag(np.diag(r))
    return np.all(np.abs(x) <= 0.5)


def make_size_reduced(r: np.ndarray) -> np.ndarray:
    r_transposed = np.copy(r.T)
    for i in range(r_transposed.shape[0]-2, -1, -1):
        for j in range(i+1, r_transposed.shape[0], 1):
            m = np.round(r_transposed[j, i])
            r_transposed[j] -= m*r_transposed[i]
    return r_transposed.T


def lovasz_condition(index: int, bstar: np.ndarray, r: np.ndarray, delta: float = 0.75) -> bool:
    lhs = np.sqrt(delta) * norm(bstar.T[index])
    rhs = norm(bstar.T[index+1] + r[index, index+1]*bstar[index])
    return lhs <= rhs


def is_delta_lll_reduced(bstar: np.ndarray, r: np.ndarray, delta: float = 0.75) -> bool:
    return is_size_reduced(r) and all([lovasz_condition(i, bstar, r, delta) for i in range(r.shape[0] - 1)])


def lll(basis: np.ndarray, delta=0.75) -> np.ndarray:
    basis_copy = np.copy(basis)
    while True:
        bstar, r = gram_schmidt_basis(basis_copy)
        reduced_r = make_size_reduced(r)
        basis_copy = bstar.dot(reduced_r)
        for i in range(bstar.shape[1]-2, -1, -1):
            if not lovasz_condition(i, bstar, reduced_r, delta=delta):
                basis_copy[:, [i, i+1]] = basis_copy[:, [i+1, i]]
                break
        else:
            break
    return basis_copy
