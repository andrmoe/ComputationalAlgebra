from prime import *
from precomputed_numbers import primes, composites
"""
I'm using pytest as my test framework. It automatically runs all functions starting with "test".
You can install pytest with "pip install pytest".
You can run all tests with "pytest test.py" in the terminal.
"""


def test_primality_test():

    for prime in primes:
        assert fermat_test(prime)
        assert trial_division_test(prime)

    for composite in composites:
        assert not fermat_test(composite)
        assert not trial_division_test(composite)


def test_find_prime():
    n = 1000
    n_min = 1 << n
    n_max = 1 << (n+1)
    for _ in range(10):
        prime = find_prime(n)
        assert n_min <= prime < n_max
        assert fermat_test(prime)
        prime = find_prime_trial_division(n)
        assert n_min <= prime < n_max
        assert fermat_test(prime)
        prime = find_prime_sieve(n)
        assert n_min <= prime < n_max
        assert fermat_test(prime)