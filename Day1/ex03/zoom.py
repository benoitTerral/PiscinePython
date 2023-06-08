from load_image import ft_load
import matplotlib.pyplot as plt
import matplotlib
import os
import numpy as np
import PIL


def main():
    try:
        os.chdir(os.path.dirname(__file__))
        matplotlib.use("WebAgg")
        img = ft_load('animal.jpeg')
        print(img)
        part_of_img = img[100:500, 450:850]
        part_of_img = np.asarray(PIL.fromarray(part_of_img).convert('L'))
        print("New shape after slicing: " + str(part_of_img.shape))
        print(part_of_img.reshape(1, np.prod(part_of_img.shape), 1))
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
