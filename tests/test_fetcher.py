"""Test fetcher script (src/fetcher.py)"""

from src import fetcher


def test_fetch1():
    """First test for fetcher function"""
    test_base_input = "USD"
    test_target_input = "GBP"

    expected_output = test_target_input / test_base_input
    actual_output = fetcher.fetch_exchange_rate(test_base_input, test_target_input)
    assert expected_output == actual_output


def test_fetch2():
    """Second test for fetcher function"""
    test_base_input = "usd"
    test_target_input = "gbp"

    expected_output = test_target_input / test_base_input
    actual_output = fetcher.fetch_exchange_rate(test_base_input, test_target_input)
    assert expected_output == actual_output


def test_fetch3():
    """Third test for fetcher function"""
    test_base_input = "egp"
    test_target_input = "eur"

    expected_output = test_target_input / test_base_input
    actual_output = fetcher.fetch_exchange_rate(test_base_input, test_target_input)
    assert expected_output == actual_output


if __name__ == "__main__":
    test_fetch1()
    test_fetch2()
    test_fetch3()
