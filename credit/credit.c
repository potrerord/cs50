// Prompts user for credit card number and reports whether it is a valid American Express, MasterCard, or Visa

#include <cs50.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>

// Gets user credit card number
long get_cc(void);

// Gets number length
int get_length(long cc);

// Checks credit card number input for validity and returns boolean value
bool checksum(long cc);

int main(void)
{
    // Prompt user for cc number
    long cc = get_cc();

    // Calculate checksum
    bool validsum = checksum(cc);

    // If valid, check card length and starting digits
    if (validsum == true)
    {
        int length = get_length(cc);
        if (length == 15)
        {
            if ((int) (cc / 10000000000000) == 34 || (int) (cc / 10000000000000) == 37)
            {
                printf("AMEX\n");
            }
            else
            {
                printf("INVALID\n");
            }
        }
        else if (length == 13)
        {
            if ((int) (cc / 1000000000000) == 4)
            {
                printf("VISA\n");
            }
            else
            {
                printf("INVALID\n");
            }
        }
        else if (length == 16)
        {
            if (cc / 1000000000000000 == 4)
            {
                printf("VISA\n");
            }
            else
            {
                if ((int) (cc / 100000000000000) < 51 || (int) (cc / 100000000000000) > 55)
                {
                    printf("INVALID\n");
                }
                else
                {
                    printf("MASTERCARD\n");
                }
            }
        }
        else
        {
            printf("CALCULATION ERROR\n");
        }
    }
    else if (validsum == false)
    {
        printf("INVALID\n");
    }
}

// Gets user credit card number
long get_cc(void)
{
    long cc;
    do
    {
        cc = get_long("Number: ");
    }
    while (cc < 0);
    return cc;
}

// Gets number length
int get_length(long cc)
{
    int length = floor(log10(cc) + 1);
    return length;
}


// Checks credit card number input for validity and returns boolean value
bool checksum(long cc)
{
    // Get length
    int length = get_length(cc);

    // Cut length in half to get every other number
    int k = (length + 1) / 2;

    // Initialize sum and tempsump/tempsum length variables
    int sum = 0;
    int tempsum = 0;
    int ts_length = 0;

    // If even length, get sum
    if (length % 2 == 0)
    {
        // Sum twice every other digit starting from second to last
        for (int i = 0; i < k; i++)
        {
            tempsum = 2 * ((long) (cc / (long) pow(10, (2 * i) + 1)) % 10);

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
            sum += (long) (cc / (long) pow(10, 2 * j)) % 10;
        }
    }

    // If odd length, get sum
    else
    {
        // Sum twice  every other digit starting from second to last
        for (int i = 0; i < k - 1; i++)
        {
            tempsum = 2 * ((long) (cc / (long) pow(10, (2 * i) + 1)) % 10);

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
            sum += (long) (cc / (long) pow(10, 2 * j)) % 10;
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