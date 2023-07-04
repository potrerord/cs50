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
    print_grid(N)

def print_grid(size):

    # For each column
    for i in range(1, size + 1):

        # Start with multiple of one hundred
        i_element = i * 100

        print("{:<6d}".format(i_element), end="")

        for j in range(i - 1, size + 1):

            j_element = i_element + (2 * j * i)
            print("{:<6d}".format(j_element), end="")
        print()


main()
