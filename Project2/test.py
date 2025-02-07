from prime import exponentiate, fermat_test, trial_division_test, find_prime, find_prime_trial_division, prime_sieve
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


def test_prime_sieve():
    # 49 is expected in the output, even though it's composite, because 7 is not sieved
    assert prime_sieve(5, 50, 3) == [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 49]
    large_num = 1 << 300
    range_size = 1000
    sieved_primes = prime_sieve(large_num, large_num + range_size)
    assert len(sieved_primes) < range_size // 2  # Make sure that sieve actually useful
    for num in range(large_num, large_num + range_size):  # Making sure that the sieve is not filtering out primes
        if num not in sieved_primes:
            assert not fermat_test(num)