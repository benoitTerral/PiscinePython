import sys

def convert_to_morse(sentence):
    morse_word = ''
    morse_dict = {
        'A':'.-',
        'B':'-...',    
        'C':'-.-.', 
        'D':'-..', 
        'E':'.',
        'F':'..-.',
        'G':'--.',
        'H':'....',
        'I':'..',
        'J':'.---',
        'K':'-.-',
        'L':'.-..',
        'M':'--',
        'N':'-.',
        'O':'---',
        'P':'.--.',
        'Q':'--.-',
        'R':'.-.',
        'S':'...',
        'T':'-',
        'U':'..-',
        'V':'...-',
        'W':'.--',
        'X':'-..-',
        'Y':'-.--',
        'Z':'--..',
        '1':'.----',
        '2':'..---',
        '3':'...--',
        '4':'....-',
        '5':'.....',
        '6':'-....',
        '7':'--...',
        '8':'---..',
        '9':'----.',
        '0':'-----',
        ', ':'--..--',
        '.':'.-.-.-',
        '?':'..--..',
        '/':'-..-.',
        '-':'-....-',
        '(':'-.--.',
        ')':'-.--.-'
    }
    for char in sentence.upper():
        if (char == ' '):
            morse_word += '/'
        else:
            morse_word += morse_dict[char]
    print(morse_word)
    return morse_word


def main():
    try:
        assert len(sys.argv) == 2, "Wrong number of arguments"
        assert all(char.isalnum() or char.isspace() for char in sys.argv[1]), "Only alphanumerics allowed"
        #words = [word for word in sys.argv[1].split()]
        morse_code = convert_to_morse(sys.argv[1])
        #for morse_word in morse_iterator:
        #    print(morse_word)
    except AssertionError as e:
        print(f"AssertionError: {str(e)}"),


if __name__ == "__main__":
    main()