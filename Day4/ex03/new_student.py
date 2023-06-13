import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate a random ID"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Create class with dataclass"""
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        self.login = self.surname
