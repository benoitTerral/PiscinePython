def callLimit(limit: int):
    """Decorator --- limiting the number of call to a function"""
    count = 0

    def callLimiter(function):
        """Passing the function"""
        def limit_function(*args: any, **kwds: any):
            """Checking the """
            nonlocal count
            if (count < limit):
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Function {function} call too many times")

        return limit_function

    return callLimiter
