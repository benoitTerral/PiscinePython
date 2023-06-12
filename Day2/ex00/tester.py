from load_csv import load
import os

os.chdir(os.path.dirname(__file__))

print("test0")
try:
    print(load("../ex00"))
except ValueError as e:
    print(f"Exception: {e}")

print("test1")
try:
    print(load("landscape.jpg"))
except ValueError as e:
    print(f"Exception: {e}")

print("test2")
try:
    print(load("life_expectancy_years.csv"))
except ValueError as e:
    print(f"Exception: {e}")
