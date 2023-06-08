from load_csv import load
import os
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd


def replace_k_with_thousand(value):
    """Receive string with k or K as a thousand indicator
    Remove the letter, multiply by 1000
    return an int as there should be not issue with trailing decimal"""
    if 'k' in value:
        value = value.replace('k', '')
        return int(float(value) * 1000)
    elif 'K' in value:
        value = value.replace('K', '')
        return int(float(value) * 1000)
    return value


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """"Identify the columns identified as object
     to map them to the remove k operation"""
    object_columns = df.select_dtypes(include='object').columns
    df[object_columns] = df[object_columns].applymap(replace_k_with_thousand)
    df[object_columns] = df[object_columns].astype(int)
    return df


def main():
    matplotlib.use("WebAgg")
    os.chdir(os.path.dirname(__file__))
    try:
        income = load(
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        life_expectancy = load(
            "life_expectancy_years.csv")
        income.set_index("country", inplace=True)
        income.columns = pd.to_datetime(income.columns)
        income = income.loc[:, income.columns >= pd.to_datetime('1900-01-01')]
        life_expectancy.set_index("country", inplace=True)
        life_expectancy.columns = pd.to_datetime(life_expectancy.columns)
        life_expectancy = life_expectancy.loc[:,
                                              (life_expectancy.columns >=
                                               pd.to_datetime('1900-01-01'))
                                              & (life_expectancy.columns <=
                                                  pd.to_datetime
                                                  ('2050-01-01'))]
        income = clean_data(income)

        plt.scatter(income[pd.to_datetime('1900-01-01')],
                    life_expectancy[pd.to_datetime('1900-01-01')])
        plt.xscale('log')
        plt.title('1900')
        plt.xlabel('Gross domestic product')
        xticks = [300, 1000, 10000]
        xticks_label = ['300', '1K', '10K']
        plt.xticks(xticks, xticks_label)
        plt.ylabel('Life Expectancy')
        plt.show()
    except ValueError as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    main()
