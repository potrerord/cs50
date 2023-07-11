"""
Prompts user for credit card number and reports whether it is a valid
American Express, MasterCard, or Visa.
"""


import re

from cs50 import get_int


def main():
    """Get change, count coins, then print count."""

    print()

    # Prompt user for cc number
    card = get_cc('Enter a credit card number: ')

    # Return if cc number is invalid.
    if not(is_valid_cc(card)):
        print('INVALID\n')
        return 1

    # Print card type.
    print(classify(card))

    print()


def classify(cc: int) -> str:
    """Return the cc type based on the length and leading digits of the
    int argument.
    """

    # Classify 13 digits as Visa.
    if len(cc) == 13:
        return 'VISA'

    # Classify 15 digits as American Express.
    elif len(cc) == 15:
        return 'AMEX'

    # Classify 16 digits as either Visa or Mastercard.
    elif len(cc) == 16:

        # Visa begins with 4.
        if str(cc)[0] == 4:
            return 'VISA'

        # Mastercard begins with 5.
        elif str(cc)[0] == 5:
            return 'MASTERCARD'


def get_cc(prompt: str) -> int:
    """Get positive user credit card number."""

    # Define constants for immediate validation checks.
    LENGTHS = [13, 15, 16]
    FIRST_DIGITS = [34, 37, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51, 52, 53,
                    54, 55]

    # Reprompt until cc with valid length and first digits is entered.
    while True:
        try:
            cc = get_int(prompt)

            # Check if number is positive.
            if cc <= 0:
                raise ValueError

            # Check number length.
            elif len(str(cc)) not in LENGTHS:
                raise ValueError

            # Check first two digits.
            elif int((str(cc)[0] + str(cc)[1])) not in FIRST_DIGITS:
                raise ValueError

        except ValueError as e:
            print('INVALID\n')

        else:
            return cc


def is_valid_cc(cc) -> bool:
    """Return boolean value indicating credit card number validity."""

    # Reverse the cc number for ease of manipulation.
    cc_reversed = str(cc)[::-1]

    # Make list of ints for every other digit starting from index 0.
    eodigit_0 = list(cc_reversed[::2])
    eodigit_0 = [int(n) for n in eodigit_0]

    # Make list of ints for every other digit starting from index 1.
    eodigit_1 = list(cc_reversed[1::2])
    eodigit_1 = [int(n) for n in eodigit_1]

    # Double every digit in the second list.
    eodigit_1_doubled = [digit * 2 for digit in eodigit_1]

    # Make new list of digits from the doubled list.
    doubled_digits = [for number in eodigit_1_doubled]

    # Add all digits.
    sum = sum(doubled_digits) + sum(eodigit_0)

    # Return True if sum ends in 0.
    if sum % 10 == 0:
        return True

    # If not, return False.
    return False


# Run the main function if script is run directly.
if __name__ == "__main__":
    main()
