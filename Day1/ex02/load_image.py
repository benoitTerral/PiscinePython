import cv2 as cv
import numpy as np
import os.path


def ft_load(path: str) -> np.ndarray:
    assert os.path.isfile(path), "File does not exist"
    img = cv.imread(path)
    assert img is not None, "File cannot be read"
    print("The shape of image is: " + str(img.shape))
    print(img)
