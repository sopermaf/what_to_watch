"""
Movie datatypes and consts
"""
from typing import Set
from dataclasses import dataclass, field
from enum import Enum, unique

# TODO: extend genre

@unique
class Genre(Enum):
    ACTION = 'action'
    COMEDY = 'comedy'
    DRAMA = 'drama'
    FANTASY = 'fantasy'
    ROMANCE = 'romance'
    SCI_FI = 'science-fiction'


@dataclass
class Movie:
    title: str
    rating: float
    genre: Set[Genre]
