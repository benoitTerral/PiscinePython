from load_image import ft_load
import os.path
import PIL


def main():
    try:
        os.chdir(os.path.dirname(__file__))
        print(ft_load("landscape.jpg"))
        return 0
    except PIL.UnidentifiedImageError as e:
        print(f"UnidentifiedImageError: {str(e)}")
    except AssertionError as e:
        print(f"AssertionError: {str(e)}")
        return 1


if __name__ == "__main__":
    main()
