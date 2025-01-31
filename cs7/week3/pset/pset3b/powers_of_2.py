"""
Prints each power of 2 from 2^0 up to maximum power, inclusive.
"""


def main():
    """Take user input and call print_powers_of_2 function."""

    print()
    num = int(input("Enter an integer greater than or equal to 0: "))
    print_powers_of_2(num)
    print()


def print_powers_of_2(power: int):
    """Print the exponentiation of 2 and all integer powers up to/
    including argument.
    """

    # Return if argument is not a nonnegative integer.
    if power < 0 or (power * 10) % 10 != 0:
        print("""error: arg for print_powers_of_2() must be a nonnegative
                 integer""")
        return

    # Initialize first iteration of 2^integer as 2^0.
    power_of_2 = 1

    # Loop for all ints from 0 to argument in one line, then new line.
    for i in range(power + 1):
        print(f"{power_of_2} ", end="")
        power_of_2 *= 2
    print()


# Run the main function if script is run directly.
if __name__ == "__main__":
    main()
