'''
Test suggest.py
'''
# pylint: disable=missing-function-docstring,unused-wildcard-import,wildcard-import

from what_to_watch.suggestion_cli import suggest
from what_to_watch.media import MediaItem
from what_to_watch.movie_data_handler import *

def test_suggest_default():
    ret = suggest(handler=MediaItemDataHandler())
    assert isinstance(ret, MediaItem)


def test_suggest_sql_lite():
    ret = suggest(handler=SQLLiteMediaItems())
    assert isinstance(ret, MediaItem)
