"""
Write a complete Python program that plays a simplified version of
the casino game Craps. This game is played with a set of two perfectly
balanced dice, each one a cube that has one side containing 1, 2, 3, 4,
5, or 6 black dots.

Your program will “roll” two dice until the total value is 4, 5, 6, 8,
9, or 10. This number becomes the player's point.

After the point value has been obtained, the program continues to roll
the dice until the total value of the dice is either:
    - 7 (in which case you lose), or
    - it's the point that was previously established (in which case you
      win).

Please use the random.randint(...) function to generate your rolls.
This problem is an exercise in implementing a solution according to the
interface of functions we have given you. Here are the functions you
need to define and use in your solution.

def do_roll():
   do_roll takes no input, rolls two dice and returns the sum of the
   roll.

def print_roll(roll_1, roll_2):
    print_roll takes the values of the two dice rolls as input and
    prints out the results to the user as shown below. It does not
    return any value.

def get_point():
    get_point takes no input, rolls until a point is established and
    returns the value of the point.

def play_from_point(point):
    play_from_point takes an integer point value and continues the game
    until the player wins or loses. It returns a Boolean value which is
    True if the player wins.

Note: it is recommended that there are two separate while loops in your
implementation of this game. Here's what the program should look like in
action:

    % python craps.py
    Computer rolls a 6 and a 5, for a total of 11.
    Computer rolls a 1 and a 2, for a total of 3.
    Computer rolls a 5 and a 1, for a total of 6.
    6 is now the established POINT.
    Computer rolls a 4 and a 4, for a total of 8.
    Computer rolls a 2 and a 5, for a total of 7.
    YOU LOSE
"""


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
