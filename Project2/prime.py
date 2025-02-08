from random import randint
import numpy as np
from typing import Generator, Callable, Iterator, Iterable
from precomputed_numbers import small_primes


def exponentiate(exponent: int, base: int, p: int) -> int:
    """
    :param exponent Must be positive
    :param base Base of the power.
    :param p Multiplication modulo this number, typically a prime
    :return Base^exponent mod p
    """
    if exponent == 0:
        return 1
    int_square_root = exponentiate(exponent >> 1, base, p)
    factor = (int_square_root * int_square_root) % p
    if exponent & 1:
        return (factor * base) % p
    else:
        return factor


def fermat_test(p: int) -> bool:
    test_numbers = range(1, min(p, 100))
    test_results = [exponentiate(p - 1, a, p) for a in test_numbers]
    return all([result == 1 for result in test_results])


def find_prime_generic(candidates: Iterator[int], test) -> int:
    while True:
        prime_candidate = next(candidates)
        if test(prime_candidate):
            return prime_candidate

def find_prime(n: int, test: Callable[[int], bool] = fermat_test) -> int:
    """
    :param n Length of the binary representation of the prime
    :param test Prime testing function
    :return A prime in the range [2^n, 2^(n+1)-1]
    """
    def random_number_gen() -> Iterator[int]:
        while True:
            yield randint(1 << n, (1 << (n + 1)) - 1)
    return find_prime_generic(random_number_gen(), test)


def generate_small_primes(n: int) -> Generator[int, None, None]:
    """
    Generates every prime number smaller than n
    """
    for m in range(n):
        if fermat_test(m):
            yield m


def trial_division_test(n: int) -> bool:
    return (all([n % p != 0 for p in small_primes]) or n in small_primes) and fermat_test(n)


def find_prime_trial_division(n: int) -> int:
    return find_prime(n, test=trial_division_test)


def prime_count_estimate(n: int) -> float:
    return (2 ** n) / (np.log(2) * n)


def prime_sieve(n_min: int, n_max: int, sieve_size=10) -> [int]:
    """
    :param n_min: Start of sieve range (inclusive)
    :param n_max: End of sieve range (exclusive)
    :param sieve_size: How many primes should be used
    :return: A list of prime candidates
    """
    numbers = list(range(n_min, n_max))
    for prime in small_primes[:sieve_size]:
        m = ((n_min + prime - 1) // prime) * prime  # Smallest multiple m of prime st. m >= n_min
        if m == prime:  # We only want to sieve out m if it is a composite number
            m += prime
        while m < n_max:
            numbers[m - n_min] = None
            m += prime
    return [n for n in numbers if n is not None]


def find_prime_sieve(n_min: int, n_max: int, sieve_size: int = 10,  test=fermat_test) -> int:
    return find_prime_generic(iter(prime_sieve(n_min, n_max, sieve_size)), test)