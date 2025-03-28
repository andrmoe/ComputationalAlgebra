import math

import numpy as np

from sympy.ntheory.residue_ntheory import sqrt_mod_iter
from sympy import primerange
from random_squares import non_trivial_lin_dep, compute_squares


def eulers_criterion(a: int, p: int) -> bool:
    return pow(a, (p-1)//2, p) == 1


def generate_factor_base(smoothness_bound: int, N: int) -> [int]:
    return [prime for prime in primerange(0, smoothness_bound) if eulers_criterion(N, prime)]


def quadratic_sieve(factor_base: [int], N: int, sieve_size: int) -> [tuple[int, dict[int, int]]]:
    root = math.isqrt(N) + 1
    sieve = [(root + n)**2 - N for n in range(sieve_size)]
    exponents = [[0 for _ in factor_base] for _ in range(sieve_size)]

    for i, p in enumerate(factor_base):
        for solution in sqrt_mod_iter(N, p):
            index = solution - root
            if index >= sieve_size:
                break
            if index < 0:
                index += (-index//p + 1)*p
            while index < sieve_size:
                sieve[index] //= p
                exponents[index][i] += 1
                index += p
    return [(root + n, exponents[n]) for n, residue in enumerate(sieve) if residue == 1]


def quadratic_sieve_factoring(N: int) -> int:
    B = int(math.exp(0.5*math.sqrt(math.log(N)*math.log(math.log(N)))))
    factor_base = generate_factor_base(B, N)
    xs, exponent_matrix = zip(*quadratic_sieve(factor_base, N, 100*len(factor_base)))
    exponent_matrix = np.array(exponent_matrix)
    lambdas, fs = non_trivial_lin_dep(exponent_matrix)
    X, Y = compute_squares(N, xs, lambdas, fs, factor_base)
    return np.gcd(X - Y, N)
