"""
Provides interface for the data
underpinning the suggestion system
linting saying too few public methods
input output error related to import from db_handler.db_connection_query
"""
#from db_handler.db_connection_query import get_media_item, get_data_from_db
from .media import MediaItem

EXAMPLE_MEDIA_ITEM = MediaItem(
    title="Space Jam",
    title_type="movie",
    rating=7.0,
    genre="action",
    language="en",
    year=1996,
    num_votes=1000,
    is_adult=False,
)

class MediaItemDataHandler:
    """
    Load, update and select movies
    """
    # pylint: disable=too-few-public-methods
    def __init__(self) -> None:
        pass # TODO: setup db connection?

    def get_random_movie(
            self,
            threshold_rating: float = 7.0,
            genre: str = 'drama',
            language: str = 'en',
    ) -> MediaItem:
        '''
        Get a random movie that matches the criteria
        '''
        # subset_imdb_data = get_data_from_db(threshold_rating, genre, language)
        # new_media_item = get_media_item(subset_imdb_data)
        return EXAMPLE_MEDIA_ITEM
