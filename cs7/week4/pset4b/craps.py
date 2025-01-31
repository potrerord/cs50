"""
Plays a simplified version of the casino game Craps between the user and
the program.
"""


from random import randint


def main():
    """Execute game by rolling dice and comparing points."""

    print()

    # Roll two dice until the total value is 4-10, which becomes the
    # player's point.
    player_point = get_point()

    # Continue to roll the dice until winner is decided.
    if play_from_point(player_point):
        print("\nYOU WIN")
    else:
        print("\nYOU LOSE")

    print()


def do_roll() -> int:
    """Take no input, roll two dice and return the sum of the roll."""

    # Roll each die.
    die1 = randint(1, 6)
    die2 = randint(1, 6)

    # Calculate sum of die rolls.
    dice_sum = die1 + die2

    # Print results of roll.
    print_roll(die1, die2)

    return dice_sum


def get_point():
    """Roll until a point between 4 and 10 (inclusive) is established,
    then return point value.
    """

    # Repeat do_roll until point value is valid.
    while True:
        point = do_roll()
        if 4 <= point <= 10 and point != 7:
            print(f"\n{point} is now the established POINT.\n")
            return point


def play_from_point(player_point: int) -> bool:
    """
    Continue the craps game until a winner is decided. Return a Boolean
    value indicating if the player won.

    Arguments:
    point -- Integer value of player's point for computer to play from.
    """

    # Continue the game from the point.
    while True:
        new_point = do_roll()
        if new_point == player_point:
            return True
        elif new_point == 7:
            return False


def print_roll(roll1, roll2) -> None:
    """Take the values of two dice rolls as input and print results for
    the user. Do not return any value.

    Arguments:
    roll1, roll2 -- integers representing the rolls.
    """

    print(f"Computer rolls a {roll1} and a {roll2}, "
          f"for a total of {roll1 + roll2}.")

if __name__ == "__main__":
    main()
