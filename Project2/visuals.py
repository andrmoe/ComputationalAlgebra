import matplotlib.pyplot as plt
import pandas as pd


def generate_sieve_plot() -> bool:
    df = pd.read_csv("temp/sieve_experiment.csv")
    df1 = df.iloc[:, 2:]
    print(df)
    print(df1)
    markers = ('o', 'v', '^', '<', '>', '8', 's', 'p', '*', 'h', 'H', 'D', 'd', 'P', 'X')
    colors = ('b', 'g', 'r', 'c', 'm', 'y')

    for (index, row), mark, color in zip(df.iterrows(), markers, colors):
        plt.scatter(df1.columns.astype(int), row[2:], color=color, label=f'n={row[1]}', marker=mark)

    plt.yscale('log')
    plt.xlabel('sieve size')
    plt.ylabel('runtime (s)')
    plt.title('Runtime for different sieve size and prime sizes')

    # Add a legend
    plt.legend()
    #plt.grid(True, which="both")
    plt.savefig("temp/sieve_plot.pdf")
    return True

def generate_optimal_sieve_size_table() -> bool:
    df = pd.read_csv("temp/sieve_experiment.csv")
    df1 = df.iloc[:, 1:]
    df_min = pd.DataFrame({
        "n": df.iloc[:, 1],
        "Smallest runtime": df1.min(axis=1),  # Get the max value of each row
        "Optimal sieve size": df1.idxmin(axis=1)  # Get the column name (label) where the max occurs
    })
    with open("temp/optimal_sieve_table.tex", "w") as f:
        f.write(df_min.to_latex())
