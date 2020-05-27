"""
Movie suggestion handling
"""
from typing import List
import sys
import pandas as pd # type: ignore
from movie_data_handler import MovieDataHandler

F_DIR = 'resources/imdb_data.csv'
ARGS = sys.argv[1:]
IMDB_DATA = pd.read_csv(F_DIR)


def suggest_movie() -> str:
    '''
    Returns a movie title as a suggestion
    '''

    movie_handler = MovieDataHandler()
    movie_handler.get_random_movie(7,'comedy','en')
    return movie_handler.media_item.title



print(suggest_movie())
#python what_to_watch/suggest/suggestion.py