def square(x: int | float) -> int | float:
    """Return square"""
    return x ** 2


def pow(x: int | float) -> int | float:
    """Return x to the power of itself"""
    return x ** x


def outer(x: int | float, function) -> object:
    """wrapper"""
    count = 0

    def inner() -> float:
        nonlocal count
        if (not count):
            count = x
        count = function(count)
        return count

    return inner
