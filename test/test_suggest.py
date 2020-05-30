'''
Test suggest.py
'''
# pylint: disable=no-function-docstring

from what_to_watch.suggestion_cli import suggest
from what_to_watch.media import MediaItem
from what_to_watch.movie_data_handler import *

def test_suggest_default():
    ret = suggest()
    assert isinstance(ret, MediaItem)


def test_suggest_sql_lite():
    ret = suggest(handler=SQLLiteMediaItems)
    assert isinstance(ret, MediaItem)
