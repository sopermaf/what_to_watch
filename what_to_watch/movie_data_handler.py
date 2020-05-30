"""
Provides interface for the data
underpinning the suggestion system
linting saying too few public methods
input output error related to import from db_handler.db_connection_query
"""
#from db_handler.db_connection_query import get_media_item, get_data_from_db
#import pyodbc
import sqlite3
from .media import MediaItem


EXAMPLE_MEDIA_ITEM = MediaItem(
    title="Space Jam",
    media_type="movie",
    rating=7.0,
    genres="action",
    language="en",
    year=1996,
    num_votes=1000,
    is_adult=False,
)

class MediaItemDataHandler:
    """
    Load, update and select movies
    """
    # pylint: disable=too-few-public-methods,unused-argument,no-self-use

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


class SQLLiteMediaItems(MediaItemDataHandler):
    '''
    For use with SQLLite DB
    '''
    def __init__(self, db_name: str = 'imdb.db'):
        super().__init__()
        self.db_name = db_name

    def get_random_movie(
            self,
            threshold_rating: float = 7.0,
            genre: str = 'drama',
            language: str = 'en',
    ) -> MediaItem:
        with sqlite3.connect(self.db_name) as conn:
            # TODO: update query with params
            # pylint: disable=unused-argument
            cursor = conn.execute('SELECT * FROM MediaItems ORDER BY RANDOM() LIMIT 1;')
            row = cursor.fetchone()
            cursor.close()

        media_item = MediaItem(*row[1:])    # ignore row id
        return media_item

    def update_db_imdb_tems(self, imdb_csv_path: str) -> None:
        '''
        Update the DB with new imdb records from
        a specified CSV file
        '''
        raise NotImplementedError
