from random import randint
from small_primes import small_primes
import numpy as np
import galois
from sympy import primerange


def trial_division_factoring(N: int, factor_base: [int]) -> [int]:
    exponents = []
    for prime in factor_base:
        power = 0
        while N % prime == 0:
            N = N//prime
            power += 1
        exponents.append(power)
    if N == 1:
        return exponents
    else:
        return None


def random_squares_stage_1(N: int, factor_base: [int]) -> tuple[np.ndarray, np.ndarray]:
    exponent_matrix = []
    xs = []
    while len(exponent_matrix) < len(factor_base) + 1:
        x = randint(1, N - 1)
        a = x ** 2 % N
        exponents = trial_division_factoring(a, factor_base)
        if exponents is not None:
            exponent_matrix.append(exponents)
            xs.append(x)
    return np.array(xs, dtype=object), np.array(exponent_matrix)


def non_trivial_lin_dep(exponent_matrix: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    GF = galois.GF(2)
    exp_matrix_mod2 = GF(exponent_matrix % 2)
    null_space = exp_matrix_mod2.T.null_space()
    lambdas = np.array(null_space[0], dtype=int)
    return lambdas, lambdas.dot(exponent_matrix) // 2


def compute_squares(N: int, xs: np.ndarray, lambdas: np.ndarray, fs: np.ndarray, factor_base: [int]) -> tuple[int, int]:
    X = np.prod([pow(int(x), int(l), N) for x, l in zip(xs, lambdas)], dtype=object) % N
    Y = np.prod([pow(p, int(f), N) for p, f in zip(factor_base, fs)], dtype=object) % N
    return X, Y


def random_squares_factoring(N: int) -> int:
    B = min(10000, N)
    factor_base = list(primerange(0, B))
    xs, exponent_matrix = random_squares_stage_1(N, factor_base)
    lambdas, fs = non_trivial_lin_dep(exponent_matrix)
    X, Y = compute_squares(N, xs, lambdas, fs, factor_base)
    return np.gcd(X-Y, N)

#print(random_squares_factoring(6089*7027))