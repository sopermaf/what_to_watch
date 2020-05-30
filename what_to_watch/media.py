"""
media item datatypes and consts, can be movie or tv series
"""
from dataclasses import dataclass

# TODO: extend genre

@dataclass(order=True)
class MediaItem:
    '''
    dataclass for a media item
    '''
    # pylint: disable=too-many-instance-attributes
    media_type: str
    title: str
    rating: float
    genres: str
    language: str
    year: int
    num_votes: int
    is_adult: bool


    def suggestion(self):
        return f"<'{self.title}', '{self.rating}/10', '{self.genres}', '{self.year}'>"