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

    // Subtract largest available coin and increment n by 1
    int coin = 25
    while (change > 0)
    {
        if (change >= coin)
        {
            change -= coin;
            n++;
        }
        else
        {
            
        }
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