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
    bool valid = checksum(cc);

    // If valid, check card length and starting digits
    if (valid == true)
    {
        int length = get_length(cc);
        if (length == 15)
        {
            printf("AMEX\n");
        }
        else if (length == 13)
        {
            printf("VISA\n");
        }
        else if (length == 16)
        {
            if (cc / 1000000000000000 == 4)
            {
                printf("VISA\n");
            }
            else
            {
                printf("MASTERCARD\n");
            }
        }
        else
        {
            printf("CALCULATION ERROR\n");
        }
    }
    else if (valid == false)
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

    // Initialize sum variable
    int sum = 0;

    // If even length, get sum
    if (length % 2 == 0)
    {
        // Sum double every other digit starting from second to last
        for (int i = 0; i < k; i++)
        {
            sum += 2 * ((int) ((double) cc / pow(10, (2 * i) + 1)) % 10);
        }

        // Sum every other digit starting from last
        for (int j = 0; j < k; j++)
        {
            sum += (int) ((double) cc / pow(10, 2 * j)) % 10;
        }
    }

    // If odd length, get sum
    else
    {
        // Sum double every other digit starting from second to last
        for (int i = 0; i < k - 1; i++)
        {
            sum += 2 * ((int) ((double) cc / pow(10, (2 * i) + 1)) % 10);
        }

        // Sum every other digit starting from last
        for (int j = 0; j < k; j++)
        {
            sum += (int) ((double) cc / pow(10, 2 * j)) % 10;
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