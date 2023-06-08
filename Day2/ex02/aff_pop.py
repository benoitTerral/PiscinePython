from load_csv import load
import os
import matplotlib.pyplot as plt
import matplotlib
import numpy as np


def main():
    matplotlib.use("WebAgg")
    os.chdir(os.path.dirname(__file__))
    try:
        dataframe = load("population_total.csv")
        print(dataframe.columns.dtype)
        pop_fr_bel = dataframe.loc[dataframe["country"]
                                   .isin(["France", "Belgium"]),
                                   :'2050']
        pop_fr_bel.set_index("country", inplace=True)
        pop_fr_bel = pop_fr_bel.replace("M", "", regex=True).astype(float)
        plt.plot(pop_fr_bel.columns.astype(int), pop_fr_bel.loc['Belgium'],
                 label='Belgium', color='blue')
        plt.plot(pop_fr_bel.columns.astype(int), pop_fr_bel.loc['France'],
                 label='France', color='green')
        plt.title('Population Projections')
        plt.xlabel('Year')
        plt.xticks(np.arange(int(min(pop_fr_bel.columns)),
                             int(max(pop_fr_bel.columns)), 40))
        yticks = np.arange(20, max(pop_fr_bel.values.ravel()), 20)
        yticks_label = [str(x) + 'M' for x in yticks]
        plt.yticks(yticks, yticks_label)
        plt.ylabel('Population')
        plt.legend(loc='lower right')
        plt.show()
    except ValueError as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    main()
