"""
Write a function named print_longer that takes two lists as input and
prints out the longer one as well as the last element of the list.

You may assume the input lists are nonempty and your function should
work with any nonempty list no matter what the size.

If the two lists are the same length, it should print
"The lists are the same length!"

To give you practice with f-strings, when printing the longer list you
may only use one print statement and it may only take one f-string as an
argument.

Demonstrate your function works by testing it in a main
function. For example,
print_longer(['chocolate', 'vanilla'], [1, 5, 9, 7])
    should print
    [1, 5, 9, 7] is the longer list and its last element is 7
"""


# Constants for main() test function.
FLAVORS = ["chocolate", "vanilla"]
NUMBERS = [1, 5, 9, 7]


def main():
    """Call print_longer function with preset arguments."""
    print()
    print_longer(FLAVORS, NUMBERS)
    print()

def print_longer(list1, list2):
    """Return and print longer list from 2 arguments."""

    # Check if lists are the same length as a special case.
    if len(list1) == len(list2):
        print("The lists are the same length!")
        return

    # Record longer list and print/return.
    elif len(list1) > len(list2):
        longer = list1

    elif len(list2) > len(list1):
        longer = list2

    print(f"{longer} is the longer list and its last element is {longer[len(longer) - 1]}")
    return longer


main()
