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


def gen_and_save_lwe(max_entry: int = 1000, epsilon: float = 0.1):
    bases = None
    with open('lattices.pkl', 'rb') as f:
        bases = pickle.load(f)
    lwe_problems = []
    for basis in bases:
        coefficients = np.random.randint(low=-max_entry, high=max_entry, size=basis.shape[0])
        error = epsilon*(2*np.random.random(basis.shape[0]) - 1)
        target = basis.dot(coefficients) + error
        lwe_problems.append((basis, coefficients, target))
    with open('lwe.pkl', 'wb') as f:
        pickle.dump(lwe_problems, f)

if __name__ == '__main__':
    gen_and_save_lwe()
