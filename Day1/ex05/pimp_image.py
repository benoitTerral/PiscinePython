import numpy as np


def ft_invert(array) -> np.array:
    """ft_invert: Invert image (225 - current value)"""
    array = np.subtract(255, array)
    return array


def ft_red(array) -> np.array:
    """ft_red: Everything turns red"""
    red_array = array.copy()
    red_array[:, :, 1:] = 0
    return red_array


def ft_green(array) -> np.array:
    """ft_green: Everything turns green"""
    green_array = array.copy()
    green_array[:, :, [0, 2]] = 0
    return green_array


def ft_blue(array) -> np.array:
    """ft_blue: Everything turns blue"""
    blue_array = array.copy()
    blue_array[:, :, 0:2] = 0
    return blue_array


def ft_grey(array) -> np.array:
    """ft_grey: Everything turns grey"""
    grey_array = array.copy()
    grey_array = np.dot(array, [0.2989, 0.5870, 0.1140])
    return grey_array.astype(np.uint8)
