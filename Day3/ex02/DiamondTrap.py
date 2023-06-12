from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Diamond class"""
    def __init__(self, first_name, is_alive=True):
        """Init Diamond class"""
        super().__init__(first_name, is_alive)

    def get_eyes(self) -> None:
        """eyes getter"""
        return self.eyes

    def set_eyes(self, color: str) -> None:
        """eyes setter"""
        self.eyes = color

    _eyes = property(get_eyes, set_eyes, doc="subclass eyes")

    def get_hairs(self) -> None:
        """hairs getter"""
        return self.hairs

    def set_hairs(self, color: str) -> None:
        """hairs setter"""
        self.hairs = color

    _hairs = property(get_hairs, set_hairs, doc="subclass hairs")
