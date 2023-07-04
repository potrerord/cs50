"""
Prints evenly-spaced triangle of values with the following specs:

- Successive rows iteratively increase in size by 1 element,
- Successive integer elements in each row iteratively increase in value
  at a constant rate of double the row number (0-indexed),
- The first element of each row is a successively greater multiple of
  100, starting with 100 and ending at 900.
"""

# Define constant for this particular problem.
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
        print("{:<6d}".format(first_in_row), end="")

        #
        for column in range(size):

            # Short circuit before the number of columns equals the
            # number of rows. There 
            if row == column:
                break
            j_element = first_in_row + (2 * (column + 1) * (row))
            print("{:<6d}".format(j_element), end="")
        print()


main()
