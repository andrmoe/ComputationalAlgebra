from prime import *
from timeit import timeit
import pandas as pd


def generate_sieve_experiment_table() -> bool:
    data = {
        "n": [10, 100, 1000]
    }
    for sieve_size in range(1, 200, 10):
        row = []
        for n in data["n"]:
            print(sieve_size, n)
            t = timeit(lambda: find_prime_sieve(n, sieve_size), number=50)
            row.append(t)
        data[str(sieve_size)] = row

    df = pd.DataFrame(data)
    df.to_csv("temp/sieve_experiment.csv")
    return True
