from prime import exponentiate, fermat_test, trial_division_test, find_prime, find_prime_trial_division
from precomputed_numbers import primes, composites


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
    n = 200
    for _ in range(3):
        prime = find_prime(n)
        assert (1 << n) <= prime < (1 << (n+1))
        assert fermat_test(prime)
        prime = find_prime_trial_division(n)
        assert (1 << n) <= prime < (1 << (n+1))
        assert fermat_test(prime)
