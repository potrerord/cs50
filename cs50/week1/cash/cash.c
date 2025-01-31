// Prints the minimum US coins (up to quarters) needed to make a given amount of change owed in cents

#include <stdio.h>
#include <cs50.h>

// Continually prompts user for positive int amount of change in cents
int get_change(void);

// Lowers input coin value to next highest coin
int lower_coin(int coin);

int main(void)
{
    // Get change owed
    int change = get_change();

    // Count number of coins with n
    int n = 0;

    // Subtract largest possible coin and increment n by 1, starting with quarter
    int coin = 25;
    while (change > 0)
    {
        // Compare change value to highest coin value and subtract/increment if possible
        if (change >= coin)
        {
            change -= coin;
            n++;
        }
        else
        {
            // Lower coin value to next highest and loop until change is 0
            coin = lower_coin(coin);
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

// Lowers coin value to next highest coin
int lower_coin(int coin)
{
    int lower = 0;
    if (coin == 25)
    {
        lower = 10;
    }
    else if (coin == 10)
    {
        lower = 5;
    }
    else if (coin == 5)
    {
        lower = 1;
    }
    else
    {
        printf("Error: invalid coin value\n");
    }
    return lower;
}