"""
Simulates drunk walk(s) from a student walking from 6th Street randomly
up or down to adjacent streets toward HOME at 1st street or JAIL at 11th
street.

Prints out a report containing the number of blocks per walked, the
student's final landing location, and the overall average number of
blocks walked per iteration.
"""


import random
from typing import Tuple


def main():
    """Run one or multiple drunk walks and print report."""

    # Constant number of drunk walks.
    WALK_COUNT = 5

    # Initialize total_block count.
    total_blocks = 0

    # Start program with new line.
    print()

    # Run WALK_COUNT drunk walks.
    for walk_number in range(1, WALK_COUNT + 1):
        # Take int and bool from drunk_walk().
        block_count, success = drunk_walk()

        total_blocks += block_count

        # Define landing location depending on bool from drunk_walk().
        if success:
            landing = "HOME"
        else:
            landing = "JAIL"

        # Print report for user.
        print(f"Here we go again... Time for walk #{walk_number}!")
        print(f"Walked {block_count} blocks, and")
        print(f"Landed in {landing}\n")

    # Print average number of blocks.
    avg_blocks = total_blocks / WALK_COUNT
    print(f"Average number of blocks: {avg_blocks}\n")


def drunk_walk() -> Tuple[int, bool]:
    """Simulate a random walk. Return a tuple containing int number of
    blocks walked and bool True if landed at home or False if jail.
    """

    # Constant position definitions.
    START = 6
    HOME = 1
    JAIL = 11

    # Initialize variables.
    position = START
    count = 0

    while True:
        # Randomly pick whether the student moves up or down one block.
        position += random.choice([-1, 1])

        # Count block movement.
        count += 1

        # If student arrives at 1st St, return True.
        if position == HOME:
            return count, True

        # If student arrives at 11th St, return False.
        elif position == JAIL:
            return count, False


if __name__ == "__main__":
    main()
