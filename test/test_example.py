'''
Example test file

New test files should be created for each module
'''
import pytest


def test_example():
    assert True


def test_example_fail():
    with pytest.raises(ValueError):
        raise ValueError
