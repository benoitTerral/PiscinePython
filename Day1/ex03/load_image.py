import cv2 as cv
import numpy as np
import os.path


def ft_load(path: str) -> np.ndarray:   
    assert os.path.isfile(path), "File does not exist"
    img = cv.imread(path)
    assert img is not None, "File cannot be read"
    gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    print("The shape of image is: " + str(gray_image.shape))
    print(gray_image)
    return (gray_image)
