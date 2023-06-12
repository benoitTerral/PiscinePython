class calculator:
    """Calculator with static methods"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        output = sum([x * y for x, y in zip(V1, V2)])
        print(output)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        output = [x + y for x, y in zip(V1, V2)]
        print(list(map(float, output)))

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        output = [x - y for x, y in zip(V1, V2)]
        print(list(map(float, output)))
