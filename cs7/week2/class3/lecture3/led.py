"""Prints an LED-style display of the digits 1-9."""

def main():
    print_led(1, 1, 1, 1, 1, 1, 1,)


def print_led(top, topleft, topright, middle, bottomleft,
              bottomright, bottom):
    """Print the LED version of the digit provided as an argument."""

    # Top:
    if top == 1:
        print(" ----")
    else:
        print()

    # Top left/right:
    for i in range(2):
        if topleft == 1:
            print("|", end="")
        else:
            print(" ", end="")
        if topright == 1:
            print("    |")
        else:
            print()

    # Middle: "----" or "    "
    if middle == 1:
        print(" ----")

    # Bottom left/right:
    for i in range(2):
        if bottomleft == 1:
            print("|", end="")
        else:
            print(" ", end="")
        if bottomright == 1:
            print("    |")
        else:
            print()

    # Bottom: "----" or "    "
    if bottom == 1:
        print(" ----")


main()