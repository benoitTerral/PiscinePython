import pandas as pd
import os


def load(path: str) -> pd.DataFrame:
    if os.path.exists(path) is None:
        return None
    dataframe = pd.read_csv('life_expectancy_years.csv')
    print(dataframe.shape)
    return dataframe
