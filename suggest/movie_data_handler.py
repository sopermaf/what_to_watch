"""
Provides interface for the data
underpinning the suggestion system
linting saying too few public methods
input output error related to import from db_handler.db_connection_query
"""
from db_handler.db_connection_query import get_media_item, get_data_from_db
from suggest.media_item import MediaItem


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
    ) -> MediaItem:
        '''
        Get a random movie that matches the criteria
        '''
        subset_imdb_data = get_data_from_db(threshold_rating, genre, language)
        new_media_item = get_media_item(subset_imdb_data)
        self.media_item = new_media_item
