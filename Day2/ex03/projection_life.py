from load_csv import load
import os
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd


def replace_k_with_thousand(value):
    if 'k' in value:
        value = value.replace('k', '')
        return int(float(value) * 1000)
    elif 'K' in value:
        value = value.replace('K', '')
        return int(float(value) * 1000)
    return value


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
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
        life_expectancy = life_expectancy.loc[:, (life_expectancy.columns >= pd.to_datetime('1900-01-01')) & (life_expectancy.columns <= pd.to_datetime('2050-01-01'))]
        # life_expectancy.drop(life_expectancy.columns[:'1900'], inplace=True)

        income = clean_data(income)
        print(income)
        print(life_expectancy)
        # print(life_expectancy.shape)
        # print(income.shape)
        # print(life_expectancy.shape)


        # income = income.applymap(replace_k_with_thousand)
        # print(income.dtypes)
        # print(dataframe.columns.dtype)
        # pop_fr_bel = dataframe.loc[dataframe["country"]
        #                            .isin(["France", "Belgium"]),
        #                            :'2050']
        # pop_fr_bel.set_index("country", inplace=True)
        # pop_fr_bel = pop_fr_bel.replace("M", "", regex=True).astype(float)
        # plt.plot(pop_fr_bel.columns.astype(int), pop_fr_bel.loc['Belgium'],
        #          label='Belgium', color='blue')
        # plt.plot(pop_fr_bel.columns.astype(int), pop_fr_bel.loc['France'],
        #          label='France', color='green')
        # plt.title('Population Projections')
        # plt.xlabel('Year')
        # plt.xticks(np.arange(int(min(pop_fr_bel.columns)),
        #                      int(max(pop_fr_bel.columns)), 40))
        # yticks = np.arange(20, max(pop_fr_bel.values.ravel()), 20)
        # yticks_label = [str(x) + 'M' for x in yticks]
        # plt.yticks(yticks, yticks_label)
        # plt.ylabel('Population')
        # plt.legend(loc='lower right')
        # plt.show()
    except ValueError as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    main()
