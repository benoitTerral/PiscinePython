class calculator:

    def __init__(self, input: list) -> None:
        """"Initiation of calcultor"""
        self.input = input

    def __add__(self, object) -> None:
        """"Add object to all element of the list"""
        output = [x + object for x in self.input]
        print(output)

    def __mul__(self, object) -> None:
        """"Multiply object to all element of the list"""
        output = [x * object for x in self.input]
        print(output)

    def __sub__(self, object) -> None:
        """"Substract object to all element of the list"""
        output = [x - object for x in self.input]
        print(output)

    def __truediv__(self, object) -> None:
        """"Divide object to all element of the list"""
        if not object:
            print("Error: division by zero")
            return None
        output = [x / object for x in self.input]
        print(output)
