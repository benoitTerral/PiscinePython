def calculate_mean(data):
    """Return mean value"""
    return sum(data) / len(data)


def sum_squared_diff(data):
    """Return sum_squared_dif for std and var"""
    mean = calculate_mean(data)
    return sum(((x - mean) ** 2 for x in data))


def compute_var(data):
    """Return variance"""
    return sum_squared_diff(data) / len(data)


def std(data):
    """Return std"""
    var = compute_var(data)
    return var ** 0.5


def ft_statistics(*args: any, **kwargs: any) -> None:
    """"Check in kwargs for expected computation (mean...)
    print the requested results"""
    statistics = {}
    for value in kwargs.values():
        try:
            sorted_args = sorted(args)
            if value == 'mean':
                statistics['mean'] = calculate_mean(args)
            if value == 'median':
                mid = len(args) // 2
                if len(args) % 2 == 0:
                    statistics['median'] = \
                        (sorted_args[mid - 1] + sorted_args[mid]) / 2
                else:
                    statistics['median'] = sorted_args[mid]
            if value == 'quartile':
                statistics['quartile'] = \
                    [float(sorted_args[int(len(args) * 0.25)]),
                     float(sorted_args[int(len(args) * 0.75)])]
            if value == 'std':
                statistics['std'] = std(args)
            if value == 'var':
                statistics['var'] = compute_var(args)
        except Exception:
            print("ERROR")
    for key, value in statistics.items():
        print(f"{key} : {value}")
