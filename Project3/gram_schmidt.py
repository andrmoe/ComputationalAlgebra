import numpy as np


def gram_schmidt_basis(basis: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    q, r = np.linalg.qr(basis)
    adjustment = np.diag(np.diag(r))
    inverse_adjustment = np.diag(1 / np.diag(r))
    return q.dot(adjustment), inverse_adjustment.dot(r)