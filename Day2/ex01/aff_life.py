from load_csv import load
import os
import matplotlib.pyplot as plt
import matplotlib
import numpy as np


def main():
    matplotlib.use("WebAgg")
    os.chdir(os.path.dirname(__file__))
    try:
        dataframe = load("life_expectancy_years.csv")
        france = dataframe.loc[dataframe["country"] == "France"]
        print(france)
        plt.plot(france.columns[1:].astype(int), france.iloc[0, 1:])
        plt.title('France life expectancy projection')
        plt.xlabel('Year')
        plt.xticks(np.arange(int(min(france.columns[1:])),
                             int(max(france.columns[1:])), 40))
        plt.ylabel('Life expectancy ')
        plt.show()
    except ValueError as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    main()
