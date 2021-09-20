# reminder to use dataclasses more often
# if not complex initialization
# saves you time from writing...
# __init__(), __repr__(), and __eq__() methods

from dataclasses import dataclass
@dataclass
class Vector:
    x: int
    y: int
    def __add__(self, other):
        return Vector(
            self.x + other.x,
            self.y + other.y,
        )
    def __sub__(self, other):
        return Vector(
            self.x - other.x,
            self.y - other.y,
        )

# for class instances to be immutable
@dataclass(frozen=True)
class FrozenVector:
    x: int
    y: int