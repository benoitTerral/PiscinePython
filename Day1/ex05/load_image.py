import numpy as np
import os.path
from PIL import Image
import matplotlib


def ft_load(path: str) -> np.ndarray:
    """"Load an image as a RGB array"""
    matplotlib.use("WebAgg")
    assert os.path.isfile(path), "File does not exist"
    img = Image.open(path)
    assert img is not None, "File cannot be read"
    img_array = np.asarray(img)
    print("The shape of image is: " + str(img_array.shape))
    return (img_array)
