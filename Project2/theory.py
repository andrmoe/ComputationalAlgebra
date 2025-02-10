import pandas as pd
import numpy as np
from precomputed_numbers import small_primes

ns = [10, 100, 1000, 10000]


def generate_data_1a():
    data = {
        "n": ns,
        "Candidates": [n * np.log(2) for n in ns]
    }

    df = pd.DataFrame(data)
    latex_table = df.to_latex(index=False)

    with open("temp/prime_trial_table.tex", "w") as f:
        f.write(latex_table)


q = 0.01


def generate_data_1b():
    data = {
        "n": ns,
        "d": [int(np.ceil(n * np.log(2) * np.log(1 / q))) for n in ns]
    }

    df = pd.DataFrame(data)
    latex_table = df.to_latex(index=False)

    with open("temp/range_size_table.tex", "w") as f:
        f.write(latex_table)


def generate_data_1c():
    data = {
        "n": ns,
    }
    for i in [0, 1, 5, 25, 100]:
        euler_product = np.prod([1 - 1 / p for p in small_primes[:i]])
        data["$d_{" + str(i) + "}$"] = [int(np.ceil(n * euler_product * np.log(2) * np.log(1 / q))) for n in ns]

    df = pd.DataFrame(data)
    latex_table = df.to_latex(index=False)

    with open("temp/sieve_table.tex", "w") as f:
        f.write(latex_table)
