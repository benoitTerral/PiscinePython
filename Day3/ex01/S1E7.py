from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name: str, is_alive=True):
        """Your docstring for Constructor"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self) -> str:
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"


class Lannister(Character):
    def __init__(self, first_name, is_alive=True):
        """Your docstring for Constructor"""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self) -> str:
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    @classmethod
    def create_lannister(cls, name, isAlive):  # should i return the names
        """Create Lanniser class method""""
        assert isinstance(name, str) and isinstance(isAlive, bool), \
            "One string and one bool expected"
        return cls(name, isAlive)
