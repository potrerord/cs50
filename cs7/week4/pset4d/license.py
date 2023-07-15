"""
Prints 20 random license plate numbers, each one consisting of three
randomly-chosen digits followed by three randomly chosen upper-case
letters. The first digit will not be zero.
"""


from random import randint


def main():
    """Print license plates."""

    # Constant number of license plate numbers to generate.
    AMOUNT = 20

    print()

    # Print plates.
    for i in range(1, AMOUNT + 1):
        print(f"{'Plate #' + str(i):>9}: {random_plate()}")

    print()


def random_capital() -> str:
    """Return a randomly selected upper-case letter."""

    # Randomly select and convert back into capital letter to return.
    return chr(randint(ord('A'), ord('Z')))


def random_plate() -> str:
    """Return one randomly selected license plate."""

    # Generate random 3-digit integer with leading zeroes. Leading digit
    # will not be 0.
    numbers = f"{randint(100, 999):>3}"

    # Generate string of 3 randomly generated capital letters.
    letters = ""
    for _ in range(3):
        letters += random_capital()

    # Return in the format "999 AAA"
    return f"{numbers} {letters}"

if __name__ == "__main__":
    main()
