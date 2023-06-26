// Prints the minimum US coins (up to quarters) needed to make a given amount of change owed in cents

#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // Get change owed in cents
    int change = get_int("Change owed: ");

    // Count number of coins with n
    int n = 0;

    // Subtract 25 cents until < 25 cents remaining, increment counter accordingly
    while (change > 24)
    {
        change -= 25;
        n ++;
    }

    // Subtract 10 cents until < 10 cents remaining, increment counter accordingly
    while (change > 9)
    {
        change -= 10;
        n ++;
    }

    // Subtract 5 cents until < 5 cents remaining, increment counter accordingly
    while (change > 4)
    {
        change -= 5;
        n ++;
    }

    // Subtract 1 cent until 0 cents remaining, increment counter accordingly
    while (change > 0)
    {
        change -= 1;
        n ++;
    }

    // Print final number of coins
    printf("%i\n", n);
}