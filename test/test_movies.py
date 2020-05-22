'''file contains modules to test modules in movies.py'''

import pytest

from what_to_watch.data_sync import movies


def test_example_job():
    '''function to test module ...'''

    assert movies.example_job() == 1


def test_example_fail():
    '''function to test module ...'''

    with pytest.raises(ValueError):
        raise ValueError
