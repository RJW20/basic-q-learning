from collections import namedtuple
from enum import Enum


class Entity(Enum):
    """Assign all entities a number for design."""

    CAT = 0
    CHEESE = 1
    MOUSE = 2
    NONE = 3

EntityCollection = namedtuple('EntityCollection', ['start', 'cats', 'cheese'])
