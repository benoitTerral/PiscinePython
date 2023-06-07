from load_image import ft_load


def main():
    try:
        ft_load('cutest-dog-breeds-jpg.jpg')
        return 0
    except AssertionError as e:
        print(f"AssertionError: {str(e)}")
        return 1


if __name__ == "__main__":
    main()
