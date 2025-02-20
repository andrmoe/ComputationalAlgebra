from lattice_search import gram_schmidt_basis
import numpy as np


def test_gram_schmidt_basis():
    basis = np.array([[0.0090681 , 0.56232371, 0.52668737],
                      [0.93955373, 0.50710907, 0.28597483],
                      [0.11046587, 0.98436934, 0.5752546 ]])
    b, r = gram_schmidt_basis(basis)
    assert np.all(np.abs(b.dot(r) - basis) < 1e-15)
    assert np.all(np.diag(r) == 1)
    for u in b.T:
        for v in b.T:
            if not np.all(u == v):
                assert abs(np.dot(u, v)/(np.linalg.norm(u)*np.linalg.norm(v))) < 1e-15



