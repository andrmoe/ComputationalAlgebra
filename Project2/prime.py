import numpy as np

def exponentiate(exponent: int, base: int, p: int) -> int:
    """
    :param exponent Must be positive
    :param base Base of the power.
    :param p Multiplication modulo this number, typically a prime
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


# for i in range(1, 200):
#     if fermat_test(i):
#         print(i)

def prime_count_estimate(n: int) -> float:
    return (2**n)/(np.log(2)*n)

for n in range(4, 8):
    print(n, prime_count_estimate(n))