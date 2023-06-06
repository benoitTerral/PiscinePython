import sys
from ft_filter import ft_filter


def main():
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        assert sys.argv[2].isdigit(), "argument is not an integer"
        words = [word for word in sys.argv[1].split()]
        selected_word = list(ft_filter(
            lambda word: len(word) > int(sys.argv[2]), words))
        print(selected_word)
    except AssertionError as e:
        print(f"AssertionError: {str(e)}")


if __name__ == "__main__":
    main()
