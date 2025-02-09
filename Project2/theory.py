import pandas as pd
import numpy as np


def generate_data_for_1a():
    ns = [10, 50, 100, 500, 1000]
    data = {
        "n": ns,
        "Candidates": [n*np.log(2) for n in ns]
    }

    df = pd.DataFrame(data)
    latex_table = df.to_latex(index=False)

    with open("prime_trial_table.tex", "w") as f:
        f.write(latex_table)

generate_data_for_1a()