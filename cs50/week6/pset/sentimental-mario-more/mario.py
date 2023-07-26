"""
Prompts user for an int height and creates a Mario-style pyramid with
# characters.
"""


def main():
    """Take user input and print pyramid."""

    # Get height of pyramid.
    height = get_height('Height: ')

    # Print pyramid.
    print_pyramid(height)


def get_height(prompt: str) -> int:
    """Return user-input positive integer pyramid height."""

    # Continually re-prompt if height is not between 1 and 8, inclusive.
    while True:
        try:
            h = int(input(prompt))
        except ValueError:
            print('error: height must be integer')
        else:
            if 1 <= h and h <= 8:
                return h

        # Reprompt user if height is not between 1 and 8.
        print('error: height must be between 1 and 8, inclusive')


def print_pyramid(height: int):
    """Print pyramid with height input."""

    # Print input number of rows, starting with row 1 to simplify calc.
    for row in range(1, height + 1):

        # Print decreasing spaces.
        print(' ' * (height - row), end='')

        # Then print increasing # starting with 1.
        print('#' * row, end='')

        # Then print a double space.
        print('  ', end='')

        # Then print the same amount of # as before.

        print('#' * row, end='')

        # Print new line after each row
        print()


if __name__ == "__main__":
    main()
