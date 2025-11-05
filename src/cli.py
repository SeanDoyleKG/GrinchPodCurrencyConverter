"""A script to import argparse module."""
import argparse

# Creating an argument parser
parser = argparse.ArgumentParser()

parser.add_argument('--base', '-b',
                    help = 'base currency')

parser.add_argument('--target', '-t',
                    help = 'target currency')

parser.add_argument('--amount', '-a',
                    type = float,
                    help = 'amount to convert')

parser.add_argument('--mock', '-m',
                    help = 'use mock data for testing',
                    action = 'store_true')

# Parse arguments
args = parser.parse_args()

# Access argument values
base_currency = args.base
target_currency = args.target
amount = args.amount
mock = args.mock


print(f"{base_currency} will be converted to {target_currency} for the amount of {amount} {base_currency}.")# This should print out: USD is converted to EUR for the amount of 100 USD.
print(type(amount))
print(type(base_currency))
print(type(target_currency))


# TODO: log when people pass in the wrong arguments for amount (e.g., a string instead of a number)

def command_line_arguments_for_currency_conversion():
    """Get currency conversion command line arguments from user.

    This function returns first the base currency, then the target currency, then the amount, and then
    whether they wish to use the mock amount.

    """
    return base_currency, target_currency, amount, mock


