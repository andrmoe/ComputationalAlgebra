import pickle

from gram_schmidt import gram_schmidt_basis
from lattice_search import search_smallest_vector
from generic_search import generic_enumeration
from lll import is_size_reduced, make_size_reduced, lovasz_condition, is_delta_lll_reduced, lll
from closest_vector import closest_vector_enumeration
import numpy as np
from typing import Iterable


def test_gram_schmidt_basis():
    basis = np.array(
        [
            [-4.7, 1.2, -0.2, 4.1, -9.2, 1.9, 9.4, -5.2, 3.9],
            [-4.3, 4.0, 1.4, 9.7, 9.7, -7.9, 3.9, -7.7, -5.1],
            [-9.7, 2.5, 8.8, 3.8, 1.4, 7.5, -6.8, -5.7, -3.5],
            [7.2, -3.2, 9.0, 8.4, 3.5, -8.2, -5.5, 3.8, 6.2],
            [-5.7, 5.8, -4.8, -4.4, 7.5, -6.6, 5.8, 4.8, 8.3],
            [-9.4, -7.5, -0.5, 5.5, -8.1, 1.3, 9.0, 3.0, -3.4],
            [-8.0, 2.3, 1.3, 6.9, 0.7, 7.3, -8.4, -3.8, -8.0],
            [5.9, -9.0, -0.9, -8.5, -7.7, 0.1, 1.7, 2.7, -9.6],
            [-8.4, 1.7, -6.4, 9.9, 2.5, -5.3, 1.0, 5.0, -7.5],
        ]
    )
    b, r = gram_schmidt_basis(basis)
    assert np.allclose(np.abs(b.dot(r) - basis), 0)
    assert np.allclose(np.diag(r), 1)
    for u in b.T:
        for v in b.T:
            if not np.all(u == v):
                assert (
                    abs(np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))) < 1e-15
                )


def test_shortest_vector():
    basis = np.array([[12, 11, 11], [12, 13, 12], [13, 13, 13]])
    shortest_vector, coefficients = search_smallest_vector(basis)
    assert np.linalg.norm(shortest_vector) == 1


def test_is_size_reduced():
    r1 = np.array([[1, 8, -3, 4], [0, 1, 5, 1], [0, 0, 1, -5], [0, 0, 0, 1]])
    assert not is_size_reduced(r1)
    r2 = np.array(
        [[1, 0.3, -0.2, 0.3], [0, 1, 0.45, -0.11], [0, 0, 1, 0.45], [0, 0, 0, 1]]
    )
    assert is_size_reduced(r2)


def test_make_size_reduced():
    basis = np.array(
        [
            [-4.7, 1.2, -0.2, 4.1, -9.2, 1.9, 9.4, -5.2, 3.9],
            [-4.3, 4.0, 1.4, 9.7, 9.7, -7.9, 3.9, -7.7, -5.1],
            [-9.7, 2.5, 8.8, 3.8, 1.4, 7.5, -6.8, -5.7, -3.5],
            [7.2, -3.2, 9.0, 8.4, 3.5, -8.2, -5.5, 3.8, 6.2],
            [-5.7, 5.8, -4.8, -4.4, 7.5, -6.6, 5.8, 4.8, 8.3],
            [-9.4, -7.5, -0.5, 5.5, -8.1, 1.3, 9.0, 3.0, -3.4],
            [-8.0, 2.3, 1.3, 6.9, 0.7, 7.3, -8.4, -3.8, -8.0],
            [5.9, -9.0, -0.9, -8.5, -7.7, 0.1, 1.7, 2.7, -9.6],
            [-8.4, 1.7, -6.4, 9.9, 2.5, -5.3, 1.0, 5.0, -7.5],
        ]
    )

    _, r1 = gram_schmidt_basis(basis)
    assert not is_size_reduced(r1)
    r2 = make_size_reduced(r1)
    assert is_size_reduced(r2)


def test_lovasz_condition():
    bstar = np.diag([4, 3, 2, 1])
    r = np.array([[1, 2, 0, 0], [0, 1, 0, 0], [0, 0, 1, -9], [0, 0, 0, 1]])

    assert lovasz_condition(0, bstar, r, 0.75)  # .75 * 4^2 <= 3^2 + 2^2 * 4^2
    assert not lovasz_condition(1, bstar, r, 0.75)  # .75 * 3^2 <= 2^2 + 0^2 * 3^2
    assert lovasz_condition(2, bstar, r, 0.75)  # .75 * 2^2 <= 1^2 + 9^2 * 2^2


def test_is_delta_lll_reduced():
    bstar = np.diag([4, 3, 2, 1])
    r1 = np.array([[1, 2, 0, 0], [0, 1, 0, 0], [0, 0, 1, -9], [0, 0, 0, 1]])
    assert not is_delta_lll_reduced(bstar, r1, 0.75)
    bstar = np.diag([4, 3, 2, 1])
    r2 = np.array([[1, 2, 0, 0], [0, 1, 4, 0], [0, 0, 1, -9], [0, 0, 0, 1]])
    assert not is_delta_lll_reduced(bstar, r2, 0.75)


def test_lll():
    basis = np.array(
        [
            [-4.7, 1.2, -0.2, 4.1, -9.2, 1.9, 9.4, -5.2, 3.9],
            [-4.3, 4.0, 1.4, 9.7, 9.7, -7.9, 3.9, -7.7, -5.1],
            [-9.7, 2.5, 8.8, 3.8, 1.4, 7.5, -6.8, -5.7, -3.5],
            [7.2, -3.2, 9.0, 8.4, 3.5, -8.2, -5.5, 3.8, 6.2],
            [-5.7, 5.8, -4.8, -4.4, 7.5, -6.6, 5.8, 4.8, 8.3],
            [-9.4, -7.5, -0.5, 5.5, -8.1, 1.3, 9.0, 3.0, -3.4],
            [-8.0, 2.3, 1.3, 6.9, 0.7, 7.3, -8.4, -3.8, -8.0],
            [5.9, -9.0, -0.9, -8.5, -7.7, 0.1, 1.7, 2.7, -9.6],
            [-8.4, 1.7, -6.4, 9.9, 2.5, -5.3, 1.0, 5.0, -7.5],
        ]
    )
    bstar, r = gram_schmidt_basis(basis)
    assert not is_delta_lll_reduced(bstar, r, 0.75)
    new_basis = lll(basis, 0.75)
    new_bstar, new_r = gram_schmidt_basis(new_basis)
    assert is_delta_lll_reduced(new_bstar, new_r, 0.75)


def test_generic_enumeration():
    target = np.array([8, 3, 4, 6, 2, 3])

    def score_func(a: [int]) -> float:
        return float(np.linalg.norm(np.array(a) - target))

    def search_range(i: int, a: [int], score_bound: float) -> Iterable[int]:
        return range(10)

    a, score = generic_enumeration(target.shape[0], 0, search_range, score_func, 10)
    assert score == 0
    assert np.all(np.array(a) == target)

def test_closest_vector_enumeration():
    basis = np.array(
        [
            [-4.7, 1.2, -0.2, 4.1, -9.2, 1.9, 9.4, -5.2, 3.9],
            [-4.3, 4.0, 1.4, 9.7, 9.7, -7.9, 3.9, -7.7, -5.1],
            [-9.7, 2.5, 8.8, 3.8, 1.4, 7.5, -6.8, -5.7, -3.5],
            [7.2, -3.2, 9.0, 8.4, 3.5, -8.2, -5.5, 3.8, 6.2],
            [-5.7, 5.8, -4.8, -4.4, 7.5, -6.6, 5.8, 4.8, 8.3],
            [-9.4, -7.5, -0.5, 5.5, -8.1, 1.3, 9.0, 3.0, -3.4],
            [-8.0, 2.3, 1.3, 6.9, 0.7, 7.3, -8.4, -3.8, -8.0],
            [5.9, -9.0, -0.9, -8.5, -7.7, 0.1, 1.7, 2.7, -9.6],
            [-8.4, 1.7, -6.4, 9.9, 2.5, -5.3, 1.0, 5.0, -7.5],
        ]
    )
    a = np.array([8, -3, 7, 0, -5, -2, 7, -1, 0])
    w = basis.dot(a) + np.array([-.03,-.03,.01,0,.045,-.09, .01, .09, -.05])
    closest_vector, coefficients = closest_vector_enumeration(basis, w)
    assert np.all(a == coefficients)


def test_lwe_examples():
    lwe_examples = None
    with open('lwe.pkl', 'rb') as f:
        lwe_examples = pickle.load(f)
    for basis, coefficients, target in lwe_examples:
        assert np.linalg.norm(basis.dot(coefficients) - target) < np.sqrt(basis.shape[0])