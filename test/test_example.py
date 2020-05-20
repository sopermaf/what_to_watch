'''
Example test file

New test files should be created for each module
'''
# pylint: disable=missing-function-docstring
import pytest


def test_example():
    assert True


def test_example_fail():
    with pytest.raises(ValueError):
        raise ValueError
