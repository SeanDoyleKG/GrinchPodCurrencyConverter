"""docstring to pass pylint"""

# pylint: disable = missing-function-docstring

from src.logger_config import setup_logging

logger = setup_logging()


def converter(amount: float, rate: float) -> float:
    if amount < 0:
        logger.error("a negative amount has been entered")
        raise ValueError("Amount must be positive")
    if amount == 0:
        logger.warning("a value of zero has been entered")
        return 0.00
    return round(amount * rate, 2)
    # rounding to 2dp because its a currency
