"""
Prints a right triangle with base on top and point in bottom right.
"""

def main():
    height = int(input("Enter height: "))
    draw(height)


def draw(height):
    """Recursively print n rows with base case of no spaces and one
    star.
    """

    stars = 1
    spaces = height - 1

    # Base case: Print a row of all stars.
    if spaces < 1:
        for i in range(stars):
            print("*", end="")
        print()
        return

    draw(stars - 1, spaces + 1)

    # Recursive case: Print previous row with one more space and one
    # fewer star.
    for i in range(spaces):
        print(" ", end="")
    for i in range(stars):
        print("*", end="")
    print()
    return

main()