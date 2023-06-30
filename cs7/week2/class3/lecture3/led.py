"""Prints an LED-style display of the digits 1-9."""

def main():
    top = 1
    topleft = 1
    topright = 1
    middle = 1
    bottomleft = 1
    bottomright = 1
    bottom = 1
    print_led()


def print_led():
    """Print the LED version of the digit provided as an argument."""

    top = 1
    topleft = 1
    topright = 1
    middle = 1
    bottomleft = 1
    bottomright = 1
    bottom = 1


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
        if topleft == 1:
            print("|", end="")
        else:
            print(" ", end="")
        if topright == 1:
            print("    |")
        else:
            print()

    # Bottom: "----" or "    "
    if bottom == 1:
        print(" ----")


main()