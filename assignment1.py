

def extended_euclidean(a: int, b: int) -> tuple[int, int]:
    if a % b == 0:
        return 0, 1
    if b % a == 0:
        return 1, 0
    # TODO: Handle negative numbers
    # gcd(a, b) = gcd(q*b + r, b) = gcd(r, b), r = a - q*b
    




def inverse(x: int, p: int) -> int:
    ...