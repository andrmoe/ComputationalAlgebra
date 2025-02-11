from prime import *
from precomputed_numbers import primes, composites
"""
I'm using pytest as my test framework. It automatically runs all functions starting with "test".
You can install pytest with "pip install pytest".
You can run all tests with "pytest test.py" in the terminal.
"""


def test_exponentiate():
    assert exponentiate(4, 3, 11) == 4


def test_primality_test():

    for prime in primes:
        assert fermat_test(prime)
        assert trial_division_test(prime)

    for composite in composites:
        assert not fermat_test(composite)
        assert not trial_division_test(composite)


def test_find_prime():
    n_min = 1 << 500
    n_max = n_min + 1000
    for _ in range(10):
        prime = find_prime(n_min, n_max)
        assert n_min <= prime < n_max
        assert fermat_test(prime)
        prime = find_prime_trial_division(n_min, n_max)
        assert n_min <= prime < n_max
        assert fermat_test(prime)
        prime = find_prime_sieve(n_min, n_max)
        assert n_min <= prime < n_max
        assert fermat_test(prime)


def test_prime_sieve():
    # 49 is expected in the output, even though it's composite, because 7 is not sieved
    assert prime_sieve(5, 50, 3) == [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 49]
    large_num = 1 << 300
    range_size = 1000
    sieved_primes = prime_sieve(large_num, large_num + range_size)
    # Make sure that sieve actually useful
    assert len(sieved_primes) < range_size // 2
    # Making sure that the sieve is not filtering out primes
    for num in range(large_num, large_num + range_size):
        if num not in sieved_primes:
            assert not fermat_test(num)