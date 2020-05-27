"""
media item datatypes and consts, can be movie or tv series
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


@unique
class Language(Enum):
    '''
    Possible language choices
    '''
    EN = 'en'
    ES = 'sp'
    FR = 'fr'


@dataclass
class Media_item:
    '''
    dataclass for a media instance
    '''
    title: str
    titleType: str
    rating: float
    genre: str
    language: str
    year: int
    num_votes: int
    is_adult: int

