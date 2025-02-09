import pandas as pd
import numpy as np


ns = [10, 100, 1000, 10000]


def generate_data_1a():
    data = {
        "n": ns,
        "Candidates": [n*np.log(2) for n in ns]
    }

    df = pd.DataFrame(data)
    latex_table = df.to_latex(index=False)

    with open("prime_trial_table.tex", "w") as f:
        f.write(latex_table)

def generate_data_1b():
    q = 0.01
    data = {
        "n": ns,
        "d": [int(np.ceil(n * np.log(2) * np.log(1 / q))) for n in ns]
    }

    df = pd.DataFrame(data)
    latex_table = df.to_latex(index=False)

    with open("range_size_table.tex", "w") as f:
        f.write(latex_table)
