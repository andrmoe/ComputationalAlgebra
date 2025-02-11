from prime import *
from timeit import timeit
import pandas as pd


def generate_experiment_table() -> bool:
    data = {
        "n": list(range(10, 100, 10)) + [500, 1000],
    }
    for algorithm in [find_prime, find_prime_trial_division, find_prime_sieve]:
        row = []
        for n in data["n"]:
            t = timeit(lambda: algorithm(n), number=100)
            row.append(t)
        data[algorithm.__name__.replace("_", " ")] = row

    df = pd.DataFrame(data)
    latex_table = df.to_latex(index=False)

    with open("temp/experiment_table.tex", "w") as f:
        f.write(latex_table)
    return True
