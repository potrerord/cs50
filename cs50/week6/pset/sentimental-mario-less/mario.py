"""
Prompts user for an int height and creates a Mario-style half-pyramid
with # characters.
"""


def main():
    """Take user input and print pyramid."""

    # Get height of half-pyramid
    height = get_height()

    # Print half-pyramid
    print_hpyramid(height)


def get_height() -> int:
    """Return user-input positive integer pyramid height."""

    # Continually re-prompt if height is not between 1 and 8, inclusive.
    while True:
        h = int(input('Height: '))
        if 1 <= h and h <= 9:
            break

        # Prompt user to reenter height.
        print('error: height must be positive integer')

    return h


def print_hpyramid(height: int):
    """Print half-pyramid with height input."""

    # Print input number of rows.
    for row in range(height):

        # In each row, print decreasing spaces starting with height - 1.
        for space in range(height - 1 - row):
            print(' ', end='')

        # Then print increasing # starting with 1.
        for block in range(row + 1):
            print('#', end='')

        # Print new line after each row
        print()


if __name__ == "__main__":
    main()
