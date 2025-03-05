import pickle

import numpy as np

from lattice_search import search_smallest_vector
from closest_vector import closest_vector_enumeration
from lll import lll


def shortest_vector_experiment():
    lwe_examples = None
    with open('lwe.pkl', 'rb') as f:
        lwe_examples = pickle.load(f)
    for basis, _, _ in lwe_examples:
        print(basis.shape[0])
        reduced_basis, u = lll(basis)
        #shortest_vector, coefficients = search_smallest_vector(basis)
        reduced_shortest_vector, reduced_coefficients = search_smallest_vector(reduced_basis)
        #print(np.linalg.norm(shortest_vector), coefficients)
        print(np.linalg.norm(reduced_shortest_vector), u.dot(reduced_coefficients))


if __name__ == '__main__':
    shortest_vector_experiment()
