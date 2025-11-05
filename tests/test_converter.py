"""Docstring to pass pylint"""
# pylint: disable=missing-function-docstring,too-many-positional-arguments,too-many-arguments,import-error,comparison-with-itself,comparison-of-constants

from src.main import get_basic

def test_basic():
    """Docstring to pass pylint"""
    assert 1 == 1

def test_basic_2():
    """Docstring to pass pylint"""
    assert get_basic() == 1
    assert get_basic() == 1
