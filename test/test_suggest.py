'''
Test suggest.py
'''
# pylint: disable=no-function-docstring

from what_to_watch.suggest import suggestion
from what_to_watch.suggest.media import MediaItem 

def test_suggest():
    ret = suggestion.suggest()
    assert isinstance(ret, MediaItem)
