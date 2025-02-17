from lattice_search import gram_schmidt_basis
import numpy as np


def test_gram_schmidt_basis():
    basis = np.array([[0.52317619, 0.85804036, 0.55523105, 0.8681827, 0.32436808],
                      [0.57127549, 0.65839771, 0.1009986, 0.12042266, 0.93052939],
                      [0.48762457, 0.07996529, 0.13134503, 0.2675712, 0.7221831],
                      [0.09749493, 0.50668113, 0.24219597, 0.81540083, 0.83598135],
                      [0.57315367, 0.16643106, 0.01186796, 0.39733132, 0.73993144]])
    b, r = gram_schmidt_basis(basis)
    for u in b:
        for v in b:
            if not np.all(np.equal(u, v)):
                assert abs(np.dot(u, v)) < 1e-15


