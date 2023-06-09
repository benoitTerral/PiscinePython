from abc import ABC, abstractmethod


class Character(ABC):
    """Your docstring for Class"""
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """Your docstring for Constructor"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Your docstring for Method"""
        self.is_alive = False

    def __str__(self) -> str:
        sb = (str(value) for value in self.__dict__.values())
        return f"Vector{{{', '.join(sb)}}}"

    def __repr__(self) -> str:
        return self.__str__()


class Stark(Character):
    """Your docstring for Class"""
    def __init__(self, first_name, is_alive=True):
        """Your docstring for Constructor"""
        super().__init__(first_name, is_alive)

    def die(self):
        """Your docstring for Method"""
        super().die()
