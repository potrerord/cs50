"""Add your solution to the problem 'craps' here."""


from random import randint


def main():
    """"""

    ...

    print("Implement me!")


def do_roll() -> int:
    """Return the sum of two simulated dice rolls."""

    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    dice_sum = die1 + die2

    return dice_sum


def get_point():
    """Return a point value from a simulated craps game."""

    ...


def play_from_point(point: int) -> bool:
    """
    Return a boolean value indicating if the player wins the craps game,
    continued using the value of point.
    """

    ...


def print_roll(roll_1, roll_2) -> None:
    """Print the results of a die roll.

    Arguments:
    roll_1, roll_2 -- integers representing the rolls.
    """

    ...


if __name__ == "__main__":
    main()
