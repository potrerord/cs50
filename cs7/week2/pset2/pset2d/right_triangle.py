"""
Prints a right triangle with base on top and point in bottom right.
"""

def main():
    height = int(input("Enter height: "))
    draw(height, 0)


def draw(blocks: int, spaces: int):
    """Recursively print n rows with base case of n - 1 spaces and one
    block.

    Default "spaces" value should be 0.
    """

    # Base case: Print n - 1 spaces followed by one block.
    if blocks <= 1:
        for i in range(spaces):
            print(" ", end="")
        print("*")
        return

    
    draw(blocks - 1, spaces + 1)

    # Recursive case: Print previous row with one more block and one
    # fewer space.
    for i in range(spaces):
        print(" ", end="")
    for i in range(blocks):
        print("#", end="")
    print()
    return

main()