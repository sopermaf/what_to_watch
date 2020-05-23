"""
Provides interface for the data
underpinning the suggestion system
"""
from typing import Union
from .movies import Genre, Movie

class MovieDataHandler:
    """
    Load, update and select movies
    """
    def __init__(self) -> None:
        raise NotImplementedError


    def get_random_movie(
            self,
            threshold_rating: float = 7.0,
            genre: Union[Genre, None] = None
    ) -> Movie:
        '''
        Get a random movie that matches the criteria
        '''
        raise NotImplementedError


    def load_data(self) -> None:
        '''
        Import movie data
        '''
        raise NotImplementedError
