"""
Prints a right triangle with base on top and point in bottom right.
"""

def main():
    height = int(input("Enter height: "))
    draw(height)


def draw(spaces: int, stars=0):
    """Recursively print n rows with base case of no spaces and all
    stars.

    Keyword arguments:
    spaces -- This is the only necessary argument 
    """

    # Base case: Print a row of all stars.
    if spaces < 1:
        for i in range(stars):
            print("*", end="")
        print()
        return

    # Draw previous row.
    draw(spaces - 1, stars + 1)

    # Recursive case: Print previous row with one more space and one
    # fewer star, stop if no stars left to print.
    if stars < 1:
        return

    for i in range(spaces):
        print(" ", end="")
    for i in range(stars):
        print("*", end="")
    print()
    return

main()