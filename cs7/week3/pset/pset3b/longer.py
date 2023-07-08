"""
Compares two lists, then prints out the longer one and its last element.
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


# Run the main function if script is run directly.
if __name__ == "__main__":
    main()
