from random import randint
import numpy as np
from typing import Generator, Callable
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


def find_prime(n: int, test: Callable[[int], bool] = fermat_test) -> int:
    """
    :param n Length of the binary representation of the prime
    :param test Prime testing function
    :return A prime in the range [2^n, 2^(n+1)-1]
    """
    prime_candidate = 4
    while not test(prime_candidate):
        prime_candidate = randint(1 << n, (1 << (n + 1)) - 1)
    return prime_candidate


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
