"""
Prints the minimum US coins (up to quarters) needed to make a given
amount of change owed in cents.
"""


from cs50 import get_float


def main():
    """Call other functions."""

    # List of coin values from quarters down.
    COIN_VALUES = [0.25, 0.10, 0.05, 0.01]

    # Get change owed.
    change = get_change('Enter change (in dollars): ')

    # Initialize counter variable.
    count = 0

    # Subtract largest possible coin and count.
    while True:




    coin = 25;
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


def get_change(prompt: str):
    """Return user-input positive int amount of change in dollars."""

    while True:
        try:
            change = get_float(prompt)
        except:
            TypeError:
            

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


# Run the main function if script is run directly.
if __name__ == "__main__":
    main()
