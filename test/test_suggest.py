'''file contains modules to test modules in suggestion.py'''

#import pytest

import pandas as pd
from what_to_watch.suggest import suggestion

DF_DATA = {'item':  ['Kazam', 'big chicken shaq'],
           'rating': ['10', '10'],
           'type': ['movie', 'tv_show']
           }

DF = pd.DataFrame(DF_DATA, columns=['item', 'rating', 'type'])
ARGS_NULL = ['movies']
ARGS_MOVIE = ['movie']
ARGS_TV_SHOW = ['tv_show']

def test_suggestion_null():
    '''function to test suggest_movie module
    should return null
    as args value is movies, not movie or tv_show'''

    assert (suggestion.suggest_movie(ARGS_NULL, DF)) == "space jam"

def test_suggestion_tvshow():
    '''function to test suggest_movie module
    should return big chicken shaq
    as args value is tv_show'''

    assert (suggestion.suggest_movie(ARGS_TV_SHOW, DF)) == "big chicken shaq"

def test_suggestion_movie():
    '''function to test suggest_movie module
    should return kazam
    as args value is movie'''

    assert (suggestion.suggest_movie(ARGS_MOVIE, DF)) == "Kazam"
