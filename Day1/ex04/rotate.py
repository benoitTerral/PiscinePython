from load_image import ft_load
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import os
import PIL


def rotate(array: np.ndarray) -> np.ndarray:
    """Rotate an array"""
    return np.asarray(list(list(x) for x in zip(*array))[::-1])


def main():
    matplotlib.use("WebAgg")
    try:
        os.chdir(os.path.dirname(__file__))
        img = ft_load('animal.jpeg')
        part_of_img = img[100:500, 450:850]
        print("The shape of image is: " + str(part_of_img.shape))
        print(part_of_img)
        part_of_img = rotate(part_of_img)
        plt.imshow(part_of_img, cmap='gray')
        plt.show()
        return 0
    except PIL.UnidentifiedImageError as e:
        print(f"UnidentifiedImageError: {str(e)}")
    except AssertionError as e:
        print(f"AssertionError: {str(e)}")
        return 1


if __name__ == "__main__":
    main()
