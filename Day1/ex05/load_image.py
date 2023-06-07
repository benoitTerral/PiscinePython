import numpy as np
import os.path
from PIL import Image
from pimp_image import ft_grey
import matplotlib.pyplot as plt
import matplotlib


def ft_load(path: str) -> np.ndarray:
    matplotlib.use("WebAgg")
    assert os.path.isfile(path), "File does not exist"
    img = Image.open(path)
    assert img is not None, "File cannot be read"
    img_array = np.asarray(img)
    grey_array = np.dot(img_array, [0.2989, 0.5870, 0.1140])
    plt.imshow(grey_array)
    plt.show()
    #print("The shape of image is: " + str(img_array.shape))
    #print(img_array)
    return (img_array)
