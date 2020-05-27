"""
Provides interface for the data
underpinning the suggestion system
"""
from typing import Union
from media_item import Media_item
import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
grand_parent_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(grand_parent_dir)
from DB_handler.db_connection_query import get_media_item

class MovieDataHandler:
    """
    Load, update and select movies
    """
    def __init__(self) -> None:
        #raise NotImplementedError
        self.media_item = None

    def get_random_movie(
            self,
            threshold_rating: float = 7.0,
            genre: str = 'drama',
            language: str = 'en',
    ) -> Media_item:
        '''
        Get a random movie that matches the criteria
        '''

        new_media_item = get_media_item(threshold_rating, genre,language)
        self.media_item = new_media_item


#python what_to_watch/suggest/movie_data_handler.py