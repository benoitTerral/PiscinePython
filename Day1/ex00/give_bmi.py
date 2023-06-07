import numpy as np


def give_bmi(
        height: list[int | float], weight: list[int | float]
        ) -> list[int | float]:
    assert all(isinstance(x, (int, float)) and x > 0 for x in height), \
        "Invalid input, only positive number accepted"
    assert all(isinstance(x, (int, float)) and x > 0 for x in weight), \
        "Invalid input, only positive numbers accepted"
    assert len(height) == len(weight), "Lists must be of the same size"
    return np.divide(weight, np.square(height)).tolist()


def apply_limit(
        bmi: list[int | float], limit: int
        ) -> list[bool]:
    assert all(isinstance(x, (int, float)) and x > 0 for x in bmi), \
        "Invalid input, only positive number accepted"
    return (np.array(bmi) > limit)
