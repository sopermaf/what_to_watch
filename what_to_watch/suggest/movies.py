"""
Movie datatypes and consts
"""
from typing import Set
from dataclasses import dataclass
from enum import Enum, unique

# TODO: extend genre

@unique
class Genre(Enum):
    '''
    Enum of media genres
    '''
    ACTION = 'action'
    COMEDY = 'comedy'
    DRAMA = 'drama'
    FANTASY = 'fantasy'
    ROMANCE = 'romance'
    SCI_FI = 'science-fiction'


@dataclass
class Movie:
    '''
    dataclass for a movie instance
    '''
    title: str
    rating: float
    genre: Set[Genre]
