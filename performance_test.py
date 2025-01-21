from typing import Generator
from assignment1 import naive_exponentiate, exponentiate
from timeit import timeit
from random import randint
import matplotlib.pyplot as plt
import numpy as np
from math import log10

def primes() -> Generator[int, None, None]:
    with open('primes.txt', 'r') as file:
        for line in file.readlines():
            yield int(line)


def performance_test(exponent=100):
    naive = []
    sq_mult = []
    for p in primes():
        base = (p - 10000) % p
        print(p, base)
        naive.append([log10(p), timeit(lambda: naive_exponentiate(exponent, base, p), number=100)])
        sq_mult.append([log10(p), timeit(lambda: exponentiate(exponent, base, p), number=100)])
    naive = np.array(naive).T
    sq_mult = np.array(sq_mult).T

    # Plot Class 1
    plt.scatter(naive[0], naive[1], color='blue', label='Naive', marker='o')

    # Plot Class 2
    plt.scatter(sq_mult[0], sq_mult[1], color='red', label='Square and multiply', marker='s')

    # Add labels and title
    plt.xlabel('log p')
    plt.ylabel('Time (s)')
    plt.title('Comparison between Naive exponentiation and "square and multiply"')

    # Add a legend
    plt.legend()

    # Show the plot
    plt.show()

if __name__ == '__main__':
    performance_test()
