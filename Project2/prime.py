from random import randint

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
    test_results = [exponentiate(p-1, a, p) for a in test_numbers]
    return all([result == 1 for result in test_results])


def find_prime(n: int) -> int:
    """
    :param n Length of the binary representation of the prime
    :return A prime in the range [2^n, 2^(n+1)-1]
    """
    prime_candidate = 4
    while not fermat_test(prime_candidate):
        prime_candidate = randint(1 << n, (1 << (n+1))-1)
    return prime_candidate