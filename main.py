"""Docstring to pass pylint"""
from cli import command_line_arguments_for_currency_conversion
from fetcher import fetch_exchange_rate, mock_fetch_exchange_rate
from converter import converter
from logger_config import setup_logging



def main():
    logger = setup_logging()

    base_currency, target_currency, amount, is_mock = command_line_arguments_for_currency_conversion()
    if not is_mock:
        exchange_rate = fetch_exchange_rate(base_currency, target_currency)
    else:
        try:
            exchange_rate = mock_fetch_exchange_rate(base_currency, target_currency)
        except Exception:
            logger.error(f"Problem getting mock data for {base_currency} -> {target_currency}")
            return
    
    new_amount = converter(amount, exchange_rate)

    
    logger.info(f"The new amount is: {new_amount} {target_currency}.")


if __name__ == "__main__":
    main()
    