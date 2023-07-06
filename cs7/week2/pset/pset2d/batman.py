"""
Prints x amount of na's followed by "... BATMAN!"
"""


# Global variable for this particular problem's na count.
NA = 16


def main():
    """Call batman() function."""
    batman(NA)


def batman(na_count: int):
    """Print x amount of na's followed by "... BATMAN!"

    Keyword argument:
    na_count -- The positive integer number of na's.
    """

    for i in range(na_count):

        # Capitalize first "na".
        if i == 0:
            print("Na ", end="")
            continue

        # Print remaining na's.
        print("na ", end="")

    # Print remaining part of phrase after na's are complete.
    print("... BATMAN!")


main()
