"""
Prints evenly-spaced triangle of values with the following specs:

- Successive rows iteratively increase in size by 1 element,
- Successive integer elements in each row iteratively increase in value
  at a constant rate of double the row number (0-indexed),
- The first element of each row is a successively greater multiple of
  100, starting with 100 and ending at 900.
"""

# Define constant number of rows for this particular problem.
N = 9


def main():
    """Call print_grid with constant N."""
    print_grid(N)

def print_grid(size):
    """Print grid of numbers."""


    for row in range(size):

        # First element in each row is multiple of 100, starting at 100.
        first_in_row = (row + 1) * 100

        # Format print to have 6 characters in each column.
        print("{:6d}".format(first_in_row), end="")

        # Begin iterating column count at 1 since the first element was
        # already printed.
        for column in range(1, size + 1):

            # Short circuit before the number of columns exceeds the
            # number of rows.
            if column > row:
                break

            # Each successive element in the row will increase by double
            # the product of the row and column indices.
            next_in_row = first_in_row + (2 * row * column)
            print("{:6d}".format(next_in_row), end="")

        # Print newline after final element.
        print()


main()
