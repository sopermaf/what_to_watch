'''
Example test file

New test files should be created for each module
'''
# pylint: disable=missing-function-docstring
import pytest

from what_to_watch.data_sync import movies


def test_example_job():
    assert movies.example_job() == 1


def test_example_fail():
    with pytest.raises(ValueError):
        raise ValueError
