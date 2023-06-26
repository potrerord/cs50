// Prompts user for credit card number and reports whether it is a valid American Express, MasterCard, or Visa

#include <cs50.h>
#include <stdio.h>
#include <bool.h>

// Gets user credit card number
long get_cc(void);

// Checks credit card number input for validity and returns boolean value
bool checksum(long cc);

int main(void)
{
    // Prompt user for cc number
    long cc = get_cc();

    // Calculate checksum
    bool valid = checksum()

    // Check card length and starting digits


    // Print card type

    // printf(AMEX\n or MASTERCARD\n or VISA\n or INVALID\n)


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

// Checks credit card number input for validity and returns boolean value
bool checksum(long cc)
{

}