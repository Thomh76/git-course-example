"""Learing git"""

from dataclasses import dataclass
from typing import NamedTuple, TypedDict


def add_number(a: int, b: int, c: int) -> int:
    """Return the sum of a, b and c."""
    return sum([a, b, c])
    # return a + b + c


def calc_difference(a: int, b: int) -> int:
    """Return difference between a and b."""
    return a - b


class Point(NamedTuple):
    """Class to keep 2D points coordinates"""

    x: int
    y: int


point_a = Point(1, 2)


class Student(TypedDict):
    name: str
    age: int
    position: Point
    friends: list["Student"]


student: Student = {"name": "Marcy", "age": 25, "position": Point(2, 3), "friends": []}


@dataclass
class point_b:
    x: int
    y: int
