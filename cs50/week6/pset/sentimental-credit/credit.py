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

    # Check if cc number is valid.
    if is_valid_cc(card):
        ...

    // If valid, check card length and starting digits
    if (validsum == true)
    {
        int length = get_length(cc);

        // 15 digits is Amex if first two digits are 34 or 37
        if (length == 15)
        {
            if ((int)(cc / 10000000000000) == 34 || (int)(cc / 10000000000000) == 37)
            {
                printf("AMEX\n");
            }
            else
            {
                printf("INVALID\n");
            }
        }

        // 13 digits is Visa if first digit is 4
        else if (length == 13)
        {
            if ((int)(cc / 1000000000000) == 4)
            {
                printf("VISA\n");
            }
            else
            {
                printf("INVALID\n");
            }
        }

        // 16 digits is Visa if first digit is 4, Mastercard if first digits are 51-55 inclusive
        else if (length == 16)
        {
            if (cc / 1000000000000000 == 4)
            {
                printf("VISA\n");
            }
            else
            {
                if ((int)(cc / 100000000000000) < 51 || (int)(cc / 100000000000000) > 55)
                {
                    printf("INVALID\n");
                }
                else
                {
                    printf("MASTERCARD\n");
                }
            }
        }

        // Any number of digits besides 13 15 16 is invalid
        else
        {
            printf("INVALID\n");
        }
    }

    // Invalid sum prints invalid
    else if (validsum == false)
    {
        printf("INVALID\n");
    }


    print()


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

        except ValueError:
            print('INVALID\n')

        else:
            return cc


def is_valid_cc(cc):
    """Return boolean value indicating credit card number validity."""

    # Reverse the cc number for ease of manipulation.
    cc_reversed = str(cc)[::-1]

    # Make list of ints for every other digit starting from index 0.
    eodigit_0 = list(int(cc_reversed[::2]))

    # Make list of ints for every other digits starting from index 1.
    eodigit_1 = list(int(cc_reversed[1::2]))

    # Double every digit in the second list.
    eodigit_1_doubled = [digit * 2 for digit in eodigit_1]

    # Make new list of digits from the doubled list.
    doubled_digits = [[int(digit) for digit in str(number)] for number in
                      eodigit_1_doubled]

    # Add all digits.
    total_sum = sum(doubled_digits) + sum(ev_oth_0)








"""
    sum = 0;
    tempsum = 0;
    ts_length = 0;

    // If even length, get sum
    if (length % 2 == 0)
    {
        // Sum twice every other digit starting from second to last
        for (int i = 0; i < k; i++)
        {
            tempsum = 2 * ((long)(cc / (long)pow(10, (2 * i) + 1)) % 10);

            // Get length of tempsum
            do
            {
                ts_length = get_length(tempsum);

                // If single digit, add to sum
                if (ts_length == 1)
                {
                    sum += tempsum;
                }

                // If not single digit, add ones digit and divide by ten, then recheck
                else
                {
                    sum += tempsum % 10;
                    tempsum /= 10;
                }
            }
            while (ts_length > 1);
        }

        // Sum every other digit starting from last
        for (int j = 0; j < k; j++)
        {
            sum += (long)(cc / (long)pow(10, 2 * j)) % 10;
        }
    }

    // If odd length, get sum
    else
    {
        // Sum twice  every other digit starting from second to last
        for (int i = 0; i < k - 1; i++)
        {
            tempsum = 2 * ((long)(cc / (long)pow(10, (2 * i) + 1)) % 10);

            // Get length of tempsum
            do
            {
                ts_length = get_length(tempsum);

                // If single digit, add to sum
                if (ts_length == 1)
                {
                    sum += tempsum;
                }

                // If not single digit, add ones digit and divide by ten, then recheck
                else
                {
                    sum += tempsum % 10;
                    tempsum /= 10;
                }
            }
            while (ts_length > 1);
        }

        // Sum every other digit starting from last
        for (int j = 0; j < k; j++)
        {
            sum += (long)(cc / (long)pow(10, 2 * j)) % 10;
        }
    }

    // Return truth value
    if (sum % 10 == 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}
"""


# Run the main function if script is run directly.
if __name__ == "__main__":
    main()
