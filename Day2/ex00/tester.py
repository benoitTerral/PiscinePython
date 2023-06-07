from load_csv import load
import os

os.chdir(os.path.dirname(__file__))
print(load("life_expectancy_years.csv"))
