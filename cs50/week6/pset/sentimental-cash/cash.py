"""
Prints the minimum US coins (up to quarters) needed to make a given
amount of change owed in cents.
"""


from cs50 import get_float


def main():
    """Get change, count coins, then print count."""

    # Get change owed.
    user_change = get_change('Enter change (in dollars): ')

    # Count coins necessary for user's change.
    coins = count_coins(user_change)

    # Print number of coins (as an integer and a newline).
    print(coins)


def get_change(prompt: str):
    """Return user-input positive int amount of change in dollars."""

    while True:
        try:
            change = get_float(prompt)
            if change < 0:
                raise ValueError('change must be positive')
        except ValueError as e:
            print('caught an exception:', e)
        else:
            return change


def count_coins(change: float) -> int:
    # List of coin values from quarters down.
    COIN_VALUES = [0.25, 0.10, 0.05, 0.01]

    # Initialize counter variable.
    count = 0

    # Iterate through list of coins.
    for coin in range(COIN_VALUES):
        while True:

            # Subtract value of each coin; count the coin.
            change -= coin
            count += 1

            # Switch to smaller coin..
            if change < coin:
                break

    # Return count when done subtracting coins.
    return count


# Run the main function if script is run directly.
if __name__ == "__main__":
    main()
