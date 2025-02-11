from prime import *
from typing import Callable
from timeit import timeit
from functools import partial
import pandas as pd


def generic_prime_finder_timer(binary_digits: int, range_size: int, search_func: Callable[[int, int], int]) -> float:
    n_min = 1 << binary_digits
    n_max = n_min + range_size
    return timeit(lambda: search_func(n_min, n_max), number=20)


def generate_experiment_table() -> bool:
    data = {
        "n": [10, 50, 100, 500],
    }
    for algorithm in [find_prime, find_prime_trial_division, find_prime_sieve]:
        data[algorithm.__name__] = [
            generic_prime_finder_timer(1 << n, 200, find_prime)
            for n in data["n"]]
    df = pd.DataFrame(data)
    latex_table = df.to_latex(index=False)

    with open("temp/experiment_table.tex", "w") as f:
        f.write(latex_table)
    return True
