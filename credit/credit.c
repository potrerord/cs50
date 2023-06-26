// Prompts user for credit card number and reports whether it is a valid American Express, MasterCard, or Visa

#include <cs50.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>

// Gets user credit card number
long get_cc(void);

// Checks credit card number input for validity and returns boolean value
bool checksum(long cc);

int main(void)
{
    // Prompt user for cc number
    long cc = get_cc();

    // Calculate checksum
    bool valid = checksum(cc);

    // If valid, check card length and starting digits
    // if (valid == true)
    // {

    // }

    // Print card type: printf(AMEX\n or MASTERCARD\n or VISA\n or INVALID\n)


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
        for (int i = 0; i < k - 1; i++)
        {
            sum += cc % (int) pow(10, 2 * (i + 1));
            sum *= 2;
        }

        // Sum every other digit starting from last
        for (int j = 0; j < k; j++)
        {
            sum += cc % (int) pow(10, 2 * j);
        }
    }

    // If odd length, get sum
    else
    {
        // Sum double every other digit starting from second to last
        for (int i = 0; i < k; i++)
        {
            sum += cc % (int) pow(10, 2 * (i + 1));
            sum *= 2;
        }

        // Sum every other digit starting from last
        for (int j = 0; j < k; j++)
        {
            sum += cc % (int) pow(10, 2 * j);
        }
    }
    printf("%i\n", sum);

    if (sum % 10 == 0)
    {
        return true;
    }
    else
    {
        return false;
    }



    // if valid return true


    // if invalid return false
}