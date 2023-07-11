"""
Prints the minimum US coins (up to quarters) needed to make a given
amount of change owed in cents.
"""


from cs50 import get_float


def main():
    """Get change, count coins, then print count."""

    print()

    # Get change owed.
    user_change = get_change('Enter change (in dollars): ')

    # Count coins necessary for user's change.
    coins = count_coins(user_change)

    # Print number of coins (as an integer and a newline).
    print(coins)

    print()


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


def count_coins(dollars: float) -> int:
    # List of coin values from quarters down.
    COIN_VALUES = [25, 10, 5, 1]

    # Convert float into integer coin value for calculations.
    cents = int(dollars * 100)

    # Initialize counter variable.
    count = 0

    # Iterate through list of coins.
    for coin in COIN_VALUES:
        while True:

            # Switch to smaller coin..
            if cents < coin:
                break

            # Subtract value of each coin; count the coin.
            cents -= coin
            count += 1

    # Return count when done subtracting coins.
    return count


# Run the main function if script is run directly.
if __name__ == "__main__":
    main()
