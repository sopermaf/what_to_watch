'''file contains modules to test modules in test_db_connection_query.py'''

from db_handler.db_connection_query import get_media_item, get_data_from_db
MOVIE_ON_NO_DATA = "space jam"

def test_return_null():
    '''function to test that if no data returned by db on request
    space jam is new_movie_item that is suggested'''

    subset_imdb_data = get_data_from_db(7, 'no genre', 'no language')
    new_media_item = get_media_item(subset_imdb_data)
    assert new_media_item.title == MOVIE_ON_NO_DATA

def test_return_media_item():
    '''function to test that if no data returned by db on request
    space jam is new_movie_item that is suggested'''

    subset_imdb_data = get_data_from_db(7, 'action', 'en')
    new_media_item = get_media_item(subset_imdb_data)
    assert new_media_item.title != MOVIE_ON_NO_DATA
