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
            p = int(line)
            if p < 1e10 and p % 10 == 1:
                yield p


def performance_test():
    naive = []
    sq_mult = []
    for p in primes():
        exponent = randint(1, p)
        base = 100
        print(p, base)
        naive.append([log10(p), log10(timeit(lambda: naive_exponentiate(exponent, base, p), number=1))])
        sq_mult.append([log10(p), log10(timeit(lambda: exponentiate(exponent, base, p), number=1))])
    naive = np.array(naive).T
    sq_mult = np.array(sq_mult).T

    # Plot Class 1
    plt.scatter(naive[0], naive[1], color='blue', label='Naive', marker='o')

    # Plot Class 2
    plt.scatter(sq_mult[0], sq_mult[1], color='red', label='Square and multiply', marker='s')

    # Add labels and title
    plt.xlabel('log p')
    plt.ylabel('log Time (s)')
    plt.title('Comparison between Naive exponentiation and "square and multiply"')

    # Add a legend
    plt.legend()

    # Show the plot
    plt.show()

if __name__ == '__main__':
    performance_test()
