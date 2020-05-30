"""
media item datatypes and consts, can be movie or tv series
"""
from dataclasses import dataclass

# TODO: extend genre

@dataclass
class MediaItem:
    '''
    dataclass for a media instance,
    pylint limit of 7 attributes is low, we need 8
    '''
    # pylint: disable=too-many-instance-attributes
    title: str
    title_type: str
    rating: float
    genre: str
    language: str
    year: int
    num_votes: int
    is_adult: bool
