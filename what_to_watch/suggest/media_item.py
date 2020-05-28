"""
media item datatypes and consts, can be movie or tv series
"""
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
class MediaItem:
    '''
    dataclass for a media instance,
    pylint limit of 7 attributes is low, we need 8
    '''
    title: str
    title_type: str
    rating: float
    genre: str
    language: str
    year: int
    num_votes: int
    is_adult: int
