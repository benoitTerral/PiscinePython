import pandas as pd
import os


def load(path: str) -> pd.DataFrame:
    if os.path.exists(path) is False or os.path.isdir(path) is True:
        return None
    try:
        dataframe = pd.read_csv(path)
    except Exception as e:
        raise ValueError(f"An Error occured while reading csv: {e}")
    print(f"Loading dataset of dimensions {dataframe.shape}")
    return dataframe
