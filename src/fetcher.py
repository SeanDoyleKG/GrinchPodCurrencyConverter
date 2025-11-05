"""This code will fetch exchange rates using an API"""

# pylint: disable=import-error

import sys
import requests
import config
from logger_config import setup_logging

ACCESS_KEY = config.ACCESS_KEY  # ACCESS_KEY = "3bd7fcd1f7687b10f1549b23dee79b74"
logger = setup_logging()


def fetch_exchange_rate(
    base: str, target: str
) -> float:  # need to update args to be CLI args
    """Fetches exchange rates from online"""
    url = (
        "http://api.exchangeratesapi.io/v1/latest?"
        + f"access_key={ACCESS_KEY}&symbols={base},{target}"
    )
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        logger.info("API request successful")
        base_rate = data["rates"].get(base)
        target_rate = data["rates"].get(target)
        return target_rate / base_rate
    except requests.RequestException as e:
        print(f"Error fetching exchange rate: {e}")
        logger.error(f"Error fetching exchange rate: {e}")
        sys.exit(1)
    except KeyError:
        print(f"Invalid target currency '{target}' or no rate available.")
        logger.error(f"Invalid target currency '{target}' or no rate available")
        sys.exit(1)
