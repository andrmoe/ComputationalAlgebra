from lattice_search import gram_schmidt_basis
import numpy as np


def test_gram_schmidt_basis():
    basis = np.array([[0.0090681 , 0.56232371, 0.52668737],
                      [0.93955373, 0.50710907, 0.28597483],
                      [0.11046587, 0.98436934, 0.5752546 ],
                      [0.80575713, 0.51523256, 0.74138081]])
    b, r = np.linalg.qr(basis)
    for u in b:
        for v in b:
            if not np.all(u == v):
                assert abs(np.dot(u, v)) < 1e-15
    assert np.all(b.dot(r) == basis)


