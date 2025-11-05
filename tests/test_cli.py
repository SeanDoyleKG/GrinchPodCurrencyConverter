import unittest
from unittest.mock import patch
from src.cli import command_line_arguments_for_currency_conversion


@patch("sys.argv", ["cli.py", "-b", "USD" "-t", "GBP", "-a", "100.00", "m"])
def test_command_line_argument_for_currency_conversion():
    x = command_line_arguments_for_currency_conversion()

    assert x == ("USD", "GBP", 100.00, True)
