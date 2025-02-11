from random import randint
from typing import Generator, Callable, Iterator, Iterable
from precomputed_numbers import small_primes


def fermat_test(p: int) -> bool:
    for _ in range(100):
        a = randint(2, p - 2)
        if pow(a, p-1, p) != 1:
            return False
    return True


def find_prime_generic(candidates: Iterator[int], test: Callable[[int], bool]) -> int:
    while True:
        prime_candidate = next(candidates)
        if test(prime_candidate):
            return prime_candidate


def find_prime(n: int, test: Callable[[int], bool] = fermat_test) -> int:
    """
    :param n Number of binary digits in the generated prime
    :param test Prime testing function
    :return A prime in the range [2^n, 2^(n+1)-1]
    """
    n_min, n_max = 1 << n, 1 << (n + 1)
    def random_number_gen() -> Iterator[int]:
        while True:
            yield randint(n_min, n_max- 1)
    return find_prime_generic(random_number_gen(), test)


def generate_small_primes(n: int) -> Generator[int, None, None]:
    """
    Generates every prime number smaller than n
    """
    for m in range(n):
        if fermat_test(m):
            yield m


def trial_division_test(n: int) -> bool:
    for p in small_primes:
        if n % p == 0 and n != p:
            return False
    return fermat_test(n)


def find_prime_trial_division(n: int) -> int:
    return find_prime(n, test=trial_division_test)


def prime_sieve(n: int, sieve_size: int = 10) -> [int]:
    """
    :param n Number of binary digits in the generated prime
    :param sieve_size: How many primes should be used
    :return: A list of prime candidates
    """
    range_size = int(6.38*n)
    n_min = 1 << n
    numbers = list(range(n_min, n_min + range_size))
    for prime in small_primes[:sieve_size]:
        # Smallest multiple m of prime st. m >= n_min
        m = ((n_min - 1) // prime + 1) * prime
        # We only want to sieve out m if it is a composite number
        if m == prime:
            m += prime
        while m < n_min + range_size:
            numbers[m - n_min] = None
            m += prime
    return [n for n in numbers if n is not None]


def find_prime_sieve(n: int, sieve_size: int = 10,  test=fermat_test) -> int:
    return find_prime_generic(iter(prime_sieve(n, sieve_size)), test)