from random import randint
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
    for _ in range(100):
        a = randint(2, p - 2)
        if exponentiate(p - 1, a, p) != 1:
            return False
    return True


def find_prime_generic(candidates: Iterator[int], test: Callable[[int], bool]) -> int:
    while True:
        prime_candidate = next(candidates)
        if test(prime_candidate):
            return prime_candidate


def find_prime(n_min: int, n_max: int, test: Callable[[int], bool] = fermat_test) -> int:
    """
    To solve the task: pass in n_min = 1 << n, n_max = (1 << (n + 1))
    :param n_min Lower bound of search range
    :param n_max Upper bound of search range (exclusive)
    :param test Prime testing function
    :return A prime in the range [2^n, 2^(n+1)-1]
    """
    def random_number_gen() -> Iterator[int]:
        while True:
            yield randint(n_min, n_max - 1)
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


def find_prime_trial_division(n_min: int, n_max: int) -> int:
    return find_prime(n_min, n_max, test=trial_division_test)


def prime_sieve(n_min: int, n_max: int, sieve_size: int = 10) -> [int]:
    """
    :param n_min: Start of sieve range (inclusive)
    :param n_max: End of sieve range (exclusive)
    :param sieve_size: How many primes should be used
    :return: A list of prime candidates
    """
    numbers = list(range(n_min, n_max))
    for prime in small_primes[:sieve_size]:
        # Smallest multiple m of prime st. m >= n_min
        m = ((n_min - 1) // prime + 1) * prime
        # We only want to sieve out m if it is a composite number
        if m == prime:
            m += prime
        while m < n_max:
            numbers[m - n_min] = None
            m += prime
    return [n for n in numbers if n is not None]


def find_prime_sieve(n_min: int, n_max: int, sieve_size: int = 10,  test=fermat_test) -> int:
    return find_prime_generic(iter(prime_sieve(n_min, n_max, sieve_size)), test)