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

    FIRST_DIGITS = [[34, 37], [4], [51, 52, 53, 54, 55]]

    while True:
        try:
            cc = get_int(prompt)

            # Check if number is positive.
            if cc <= 0:
                raise ValueError('cc number must be positive')

            # Check number length.
            elif len(str(cc)) not in (13, 15, 16):
                raise ValueError('cc number must have 13/15/16 digits')

            elif str(cc)[0] not in (3, 4, 5):
                raise ValueError('cc number must begin with 3, 4, or 5')

            elif str(cc)[0]

        except ValueError as e:
            print('caught exception:', e, '\n')

        else:
            return cc


bool is_valid_cc(cc)
    """Return boolean value indicating credit card number validity."""

    # Cut length in half to get every other number

    # Initialize sum and tempsump/tempsum length variables
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



# Run the main function if script is run directly.
if __name__ == "__main__":
    main()
