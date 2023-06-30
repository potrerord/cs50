"""Prints an LED-style display of the digits 1-9."""

def main():
    print_led()


def print_led():
    """Print the LED version of the digit provided as an argument."""

    # Top:
    print(" ", end="")
    print("----")

    # Top left/right:
    print("|\n|")

    # Middle: "----" or "    "
    print(" ", end="")
    print("----")

    # Bottom left/right:
    print("|\n|")

    # Bottom: "----" or "    "
    print(" ", end="")
    print("----")


main()