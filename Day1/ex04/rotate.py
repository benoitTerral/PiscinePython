from load_image import ft_load
import matplotlib.pyplot as plt
import matplotlib
import numpy as np


def main():
    matplotlib.use("WebAgg")
    try:
        img = ft_load(
            '/nfs/homes/bterral/Documents/github/PiscinePython/Day1/ex03/animal.jpeg')
        part_of_img = img[100:500, 450:850]
        part_of_img = np.transpose(part_of_img)
        print("New shape after Transpose: " + str(part_of_img.shape))
        print(part_of_img)
        plt.imshow(part_of_img, cmap='gray')
        plt.show()
        return 0
    except AssertionError as e:
        print(f"AssertionError: {str(e)}")
        return 1


if __name__ == "__main__":
    main()
