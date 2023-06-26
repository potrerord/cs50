// Prints the minimum US coins (up to quarters) needed to make a given amount of change owed in cents

#include <stdio.h>
#include <cs50.h>

// Continually prompts user for positive int amount of change in cents
int get_change(void);

int main(void)
{
    // Get change owed
    int change = get_change();

    // Count number of coins with n
    int n = 0;

    // Subtract 25 cents until < 25 cents remaining, increment counter accordingly
    while (change >= 25)
    {
        change -= 25;
        n ++;
    }

    // Subtract 10 cents until < 10 cents remaining, increment counter accordingly
    while (change >= 10)
    {
        change -= 10;
        n ++;
    }

    // Subtract 5 cents until < 5 cents remaining, increment counter accordingly
    while (change >= 5)
    {
        change -= 5;
        n ++;
    }

    // Subtract 1 cent until 0 cents remaining, increment counter accordingly
    while (change >= 1)
    {
        change -= 1;
        n ++;
    }

    // Print final number of coins
    printf("%i\n", n);
}

// Continually prompts user for positive int amount of change in cents
int get_change(void)
{
    int change;
    do
    {
        change = get_int("Change owed: ");
    }
    while (change < 0);
    return change;
}