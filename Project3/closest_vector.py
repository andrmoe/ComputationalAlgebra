import numpy as np


def babai_rounding(lattice_basis: np.ndarray, point: np.ndarray) -> np.ndarray:
    a = np.linalg.solve(lattice_basis, point)
    a = np.round(a)
    return lattice_basis.dot(a)
