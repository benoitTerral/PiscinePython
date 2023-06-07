import sys


def get_string():
    """Check tnb of arguments:
    - error if more than one
    - parse if one
    - prompt if 0
    """
    assert (len(sys.argv) < 3), "Too many arguments provided"
    if len(sys.argv) == 1 or sys.argv[1] is None:
        print("What is the text to count?")
        user_input = sys.stdin.readline()
        print(user_input)
        return (user_input)
    else:
        assert isinstance(sys.argv[1], str), "Argument is not a string"
        return sys.argv[1]


def print_number_of_char(text):
    """Compute nb of words,upper-case, lower-case, punctuation"""
    counts = {
        'total': 0,
        'upper_case': 0,
        'lower_case': 0,
        'punctuation': 0,
        'digits': 0,
        'spaces': 0
    }
    for char in text:
        counts['total'] += 1
        if char.isupper():
            counts['upper_case'] += 1
        elif char.islower():
            counts['lower_case'] += 1
        elif char.isdigit():
            counts['digits'] += 1
        elif char.isspace():
            counts['spaces'] += 1
        else:
            counts['punctuation'] += 1
    counts['spaces'] += text.count(chr(4))
    return counts


def nice_print(counts):
    """Print results stored in the dictionary"""
    print(f"The text contains {counts['total']} characters:")
    print(f"{counts['upper_case']} upper letters")
    print(f"{counts['lower_case']} lower letters")
    print(f"{counts['punctuation']} punctuation marks")
    print(f"{counts['spaces']} spaces")
    print(f"{counts['digits']} digits")


def main():
    try:
        text = get_string()
        counts = print_number_of_char(text)
        nice_print(counts)
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt detected. Program ended.")
        return 1
    except AssertionError as e:
        print(f"AssertionError: {str(e)}")
        return 1
    return 0


if __name__ == "__main__":
    main()
