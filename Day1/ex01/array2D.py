import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    assert isinstance(family, list), "list of lists is expected as input"
    assert all(isinstance(family[0], list) and
               len(sublist) == len(family[0])
               for sublist in family), "list of lists is expected as input"
    array = np.array(family)
    print("My shape is : " + str(array.shape))
    array = array[start:end]
    print("My new shape is : " + str(array.shape))
    return array.tolist()
