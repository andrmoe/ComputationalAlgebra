from sys import int_info


# 1
def add(a: int, b: int, p: int) -> int:
    return (a + b) % p


def sub(a: int, b: int, p: int) -> int:
    return (a - b) % p


def mul(a: int, b: int, p: int) -> int:
    return (a*b) % p


def extended_euclidean(a: int, b: int) -> tuple[int, int]:
    if a < b:
        k2, k1 = extended_euclidean(b, a)
        return k1, k2
    if a % b == 0:
        return 0, 1
    # TODO: Handle negative numbers
    # gcd(a, b) = gcd(q*b + r, b) = gcd(r, b), r = a - q*b
    # gcd(b, r) = k1*b + k2*r
    # gcd(a, b) = k1*b + k2*(a - q*b) = k2*a + (k1 - q*k2)*b
    q, r = divmod(a, b)
    k2, k1 = extended_euclidean(r, b)
    return k2, k1-q*k2


def inverse(x: int, p: int) -> int:
    # k1*x + k2*p = gcd(x, p) = 1, answer is k1
    k1, k2 = extended_euclidean(x, p)
    return k1


# 2
def naive_exponentiate(exponent: int, base: int, p: int) -> int:
    if exponent < 0:
        base_inverse = inverse(base, p)
        return exponentiate(-exponent, base_inverse, p)
    result = 1
    for _ in range(exponent):
        result = mul(result, base, p)
    return result


def exponentiate(exponent: int, base: int, p: int) -> int:
    if exponent < 0:
        base_inverse = inverse(base, p)
        return exponentiate(-exponent, base_inverse, p)
    if exponent == 0:
        return 1
    int_square_root = exponentiate(exponent >> 1, base, p)
    factor = mul(int_square_root, int_square_root, p)
    if exponent & 1:
        return mul(factor, base, p)
    else:
        return factor
