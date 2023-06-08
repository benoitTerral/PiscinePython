from load_csv import load
import os

os.chdir(os.path.dirname(__file__))

try:
    print(load("../ex00"))
except ValueError as e:
    print(f"Exception: {e}")

try:
    print(load("../../Day1/ex05/landscape.jpg"))
except ValueError as e:
    print(f"Exception: {e}")

try:
    print(load("life_expectancy_years.csv"))
except ValueError as e:
    print(f"Exception: {e}")
