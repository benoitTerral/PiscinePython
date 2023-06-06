def check_even(number):
    if number % 2 == 0:
          return True  

    return False


def ft_filter(func, iter):
    return [item for item in iter if func(item)]


def main():
    try:
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        filter_iterator = filter(check_even, numbers)
        filter_numbers = list(filter_iterator)

        ft_filter_iterator = ft_filter(check_even, numbers)
        ft_filter_numbers = list(ft_filter_iterator)

        print(f'filter list {filter_numbers}')
        print(f'filter list {ft_filter_numbers}')
    except TypeError as e:
         print(f"TypeError: {str(e)}")

if __name__ == "__main__":
    main()
