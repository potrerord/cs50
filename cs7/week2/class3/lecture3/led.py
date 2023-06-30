"""Prints an LED-style display of the digits 1-9."""

def main():
    """Print digits according to manually-coded on/off codes.

    Forever loop for testing purposes.
    """

    while True:
        digit = int(input("Enter digit: "))

        if digit == 0:
            print_led(1, 1, 1, 0, 1, 1, 1)
        elif digit == 1:
            print_led(0, 0, 1, 0, 0, 1, 0)
        elif digit == 2:
            print_led(1, 0, 1, 1, 1, 0, 1)
        elif digit == 3:
            print_led(1, 0, 1, 1, 0, 1, 1)
        elif digit == 4:
            print_led(0, 1, 1, 1, 0, 1, 0)
        elif digit == 5:
            print_led(1, 1, 0, 1, 0, 1, 1)
        elif digit == 6:
            print_led(1, 1, 0, 1, 1, 1, 1)
        elif digit == 7:
            print_led(1, 0, 1, 0, 0, 1, 0)
        elif digit == 8:
            print_led(1, 1, 1, 1, 1, 1, 1)
        elif digit == 9:
            print_led(1, 1, 1, 1, 0, 1, 1)


def print_led(top, topleft, topright, middle, bottomleft,
              bottomright, bottom):
    """Print the LED version of the digit provided as an argument.

    Arguments designate whether LED segment is "on" with 1 or "off" with
    2.
    """

    # Top
    if top == 1:
        print(" ----")
    else:
        print()

    # Top left/right
    for i in range(2):
        if topleft == 1:
            print("|", end="")
        else:
            print(" ", end="")
        if topright == 1:
            print("    |")
        else:
            print()

    # Middle
    if middle == 1:
        print(" ----")
    else:
        print()

    # Bottom left/right
    for i in range(2):
        if bottomleft == 1:
            print("|", end="")
        else:
            print(" ", end="")
        if bottomright == 1:
            print("    |")
        else:
            print()

    # Bottom
    if bottom == 1:
        print(" ----")
    else:
        print()


main()