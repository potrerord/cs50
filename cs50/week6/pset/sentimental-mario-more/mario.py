"""
Prompts user for an int height and creates a Mario-style half-pyramid
with # characters.
"""


def main():
    """Take user input and print pyramid."""

    # Get height of half-pyramid
    height = get_height('Height: ')

    # Print half-pyramid
    print_hpyramid(height)


def get_height(prompt: str) -> int:
    """Return user-input positive integer pyramid height."""

    # Continually re-prompt if height is not between 1 and 8, inclusive.
    while True:
        try:
            h = int(input(prompt))
            if 1 <= h and h <= 8:
                return h
        except ValueError:
            print('error: height must be between 1 and 8, inclusive')


def print_hpyramid(height: int):
    """Print half-pyramid with height input."""

    # Print input number of rows, starting with row 1 to simplify calc.
    for row in range(1, height + 1):

        # Print decreasing spaces.
        print(' ' * (height - row), end='')

        # Then print increasing # starting with 1.
        print('#' * row, end='')

        # Print new line after each row
        print()


if __name__ == "__main__":
    main()
