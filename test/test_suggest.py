'''
Example test file

New test files should be created for each module
'''
# pylint: disable=missing-function-docstring
from what_to_watch.suggest import suggestion


def test_example_job():
    assert suggestion.suggest_movie() == "Space Jam"
