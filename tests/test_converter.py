"""Docstring to pass pylint"""

# pylint: disable=missing-function-docstring,too-many-positional-arguments,too-many-arguments,import-error,comparison-with-itself,comparison-of-constants

# from src.main import get_basic


# def test_basic():
#     """Docstring to pass pylint"""
#     assert 1 == 1


# def test_basic_2():
#     """Docstring to pass pylint"""
#     assert get_basic() == 1
#     assert get_basic() == 1

import pytest
from src.converter import converter

def test_converter_positive():
    #arrange 
    amount = 100
    rate = 1.2 #chnage this later to use mock_rates
    expected_output = 120.00
    #act
    actual_output = converter(amount, rate)
    #assert
    assert actual_output == expected_output

def test_converter_zero_amount():
    #arrange 
    amount = 0
    rate = 1.2 #chnage this later to use mock_rates
    expected_output = 0.00
    #act
    actual_output = converter(amount, rate)
    #assert
    assert actual_output == expected_output

def test_converter_rounding():
    #arrange 
    amount = 100
    rate = 1.222222222 #chnage this later to use mock_rates
    expected_output = 122.22
    #act
    actual_output = converter(amount, rate)
    #assert
    assert actual_output == expected_output

def test_converter_negative():
    amount = -100
    rate = 1.20
    #act
    with pytest.raises(ValueError):
        converter(amount,rate)

