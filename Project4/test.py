from random_squares import trial_division_factoring
from quadratic_sieve import quadratic_sieve, eulers_criterion, generate_factor_base

import numpy as np

def test_trial_division_factoring():
    factor_base = [2, 3, 5, 7, 11, 13]
    assert trial_division_factoring(5, factor_base) == [0, 0, 1, 0, 0, 0]
    assert trial_division_factoring(2*3**3*7, factor_base) == [1, 3, 0, 1, 0, 0]
    assert trial_division_factoring(7**100, factor_base) == [0, 0, 0, 100, 0, 0]
    assert trial_division_factoring(17, factor_base) is None


def test_quadratic_sieve_factor_base():
    N = 5657*7757
    factor_base = generate_factor_base(100, N)
    for p in factor_base:
        assert eulers_criterion(N, p)


def test_quadratic_sieve():
    N = 5657 * 7757
    factor_base = generate_factor_base(1000, N)
    result = quadratic_sieve(factor_base, N, 10*len(factor_base))
    for x, factorisation in result:
        assert x**2 - N == np.prod([p**r for p, r in zip(factor_base, factorisation)], dtype=object)

