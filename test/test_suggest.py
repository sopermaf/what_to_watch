'''file contains modules to test modules in suggestion.py'''

from what_to_watch.suggest import suggestion

MOVIE_ON_NO_DATA = "space jam"


def test_suggestion_movie_correct_params():
    '''function to test suggest_movie modules
    should return kazam
    as args value is movie'''

    threshold_rating = 7
    genre = 'action'
    language = 'en'
    assert (suggest_movie(threshold_rating, genre, language)) != MOVIE_ON_NO_DATA


def test_suggestion_movie_false_params():
    '''function to test suggest_movie module
    should return kazam
    as args value is movie'''
    threshold_rating = 7
    genre = 'fake'
    language = 'fake'
    assert (suggest_movie(threshold_rating, genre, language)) == MOVIE_ON_NO_DATA
