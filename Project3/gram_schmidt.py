import numpy as np
from fontTools.misc.cython import returns


def gram_schmidt_basis(basis: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    q, r = np.linalg.qr(basis)
    adjustment = np.diag(np.diag(r))
    inverse_adjustment = np.diag(1 / np.diag(r))
    return q.dot(adjustment), inverse_adjustment.dot(r)


def orthogonality_defect(basis: np.ndarray) -> float:
    bstar, _ = gram_schmidt_basis(basis)
    return np.prod(np.linalg.norm(basis, axis=0)/np.linalg.norm(bstar, axis=0))
