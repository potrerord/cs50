"""
A Harvard student has decided to celebrate just graduating by getting a
bit smashed.

Their home is at 1st Street and Main Street, and the jail is at 11th
Street and Main Street. The student starts at 6th Street and Main Street
and randomly chooses to wander one block up or down Main Street with
equal probability, 0.5. At each intersection they repeat the process
until arriving safely at home or landing in jail. That is, at each
intersection, the drunk student has a 50-50 probability of staggering a
block one way or the other, to the next higher-numbered or next lower-
numbered street.

Write a function named drunk_walk() using a while loop that simulates
the drunk student's walk; your function should return a list or a tuple
with an integer that indicates how many blocks were walked as well as a
Boolean that indicates whether they ended up at home or in jail. The
function drunk_walk should not print out anything. Your program should
print out how many blocks were walked and where the student landed. You
should not print out each step taken in your final version of the
function, though you might want to do this while you are debugging.

Once you have your function working, have your main program call upon
your drunk_walk() function N times. Finally, have it calculate and print
the average number of blocks that the student took for one trip, to one
decimal place. Here's what your program might look like in action, with
N equal to 5:
       Here we go again... time for a walk!
       Walked 37 blocks, and
       Landed at HOME
       Here we go again... time for a walk!
       Walked 19 blocks, and
       Landed in JAIL
       Here we go again... time for a walk!
       Walked 13 blocks, and
       Landed in JAIL
       Here we go again... time for a walk!
       Walked 25 blocks, and
       Landed in JAIL
       Here we go again... time for a walk!
       Walked 15 blocks, and
       Landed at HOME
       Average # of blocks equals 21.8
"""


import random
from typing import Tuple


def main():
    """asdf."""


    if drunk_walk():
        landing = "HOME"
    else:
        landing = "JAIL"

    print("\nHere we go again... Time for a walk!")
    print(f"Walked {} blocks, and")
    print(f"Landed in {landing}")


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
            return (count, True)

        # If student arrives at 11th St, return False.
        elif position == JAIL:
            return (count, False)


if __name__ == "__main__":
    main()
