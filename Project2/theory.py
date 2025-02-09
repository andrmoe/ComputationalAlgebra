import pandas as pd
import numpy as np


def generate_data_for_1a():
    ns = [10, 50, 100, 500, 1000]
    data = {
        "n": ns,
        "Candidates": [n*np.log(2) for n in ns]
    }

    df = pd.DataFrame(data)
    latex_table = df.to_latex(index=False, label="tab:exp_candidates")

    with open("table.tex", "w") as f:
        f.write(latex_table)
