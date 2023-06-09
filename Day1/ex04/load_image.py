import cv2 as cv
import numpy as np
import os.path


def ft_load(path: str) -> np.ndarray:
    """"Load an image as a RGB array"""
    assert os.path.isfile(path), "File does not exist"
    img = cv.imread(path)
    gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    assert img is not None, "File cannot be read"
    return (gray_image)
