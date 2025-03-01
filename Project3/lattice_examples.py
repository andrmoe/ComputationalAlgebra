import numpy as np
from gram_schmidt import orthogonality_defect


lattice_examples = [

]

def generate_example(dim: int, max_entry: int = 1000, tries=10000):
    worst_basis = np.eye(dim)
    for _ in range(tries):
        ex = np.random.randint(low=-10*max_entry, high=10*max_entry, size=(dim, dim))/10
        if orthogonality_defect(ex) > orthogonality_defect(worst_basis):
            worst_basis = ex
    return worst_basis
