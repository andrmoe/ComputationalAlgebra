import numpy as np
from gram_schmidt import orthogonality_defect
import pickle


def generate_example(dim: int, max_entry: int = 1000, tries=100):
    worst_basis = np.eye(dim)
    for _ in range(tries):
        ex = np.random.randint(low=-10*max_entry, high=10*max_entry, size=(dim, dim))/10
        if orthogonality_defect(ex) > orthogonality_defect(worst_basis):
            worst_basis = ex
    return worst_basis


def gen_and_save_examples():
    examples = []
    for dim in range(50, 801, 50):
        print(dim)
        examples.append(generate_example(dim))
    with open('lattices.pkl', 'wb') as f:
        pickle.dump(examples, f)


if __name__ == '__main__':
    gen_and_save_examples()