"""
Prints a box with user-input size.

Example of size 3: +--+
                   |  |
                   +--+
"""


def main():
    """Execute program, call all other functions and loop program
    if user desires.
    """

    while True:
        # Prompt user for size and draw box.
        user_size = get_size()
        print()
        draw_box(user_size)

        # Ask user if they would like to run program again, then loop
        # accordingly.
        user_redo = get_redo()
        if user_redo == False:
            print()
            return
        else:
            pass


def get_size() -> int:
    """Prompt user for size and continually reprompt if input is not a
    positive integer. Return positive integer.
    """

    while True:
        user_input = input("\nEnter a size: ")
        if user_input.isdigit() and int(user_input) > 0:
            return int(user_input)
        print("Size must be a positive integer.")


def draw_box(size: int):
    """Take integer argument for size and draw box according to size.

    Keyword argument:
    size -- The number of rows and columns for the box.
    """

    # Print a + character to represent a size 1 box.
    if size == 1:
        print("+")

    else:

        # Range starts at 1 to use row number in calculations.
        for row in range(1, size + 1):

            # Defines end/middle "characters" depending on row. mid_char
            # uses two of each character to more closely approximate the
            # height of a line of text.
            if row == 1 or row == size:
                end_char = "+"
                mid_char = "--"
            else:
                end_char = "|"
                mid_char = "  "

            # Print end+middle+end for each row.
            # Middle is reduced by 2 to account for 2 end characters.
            print(end_char + mid_char * (size - 2) + end_char)


def get_redo() -> bool:
    """Prompt user to loop program if they wish, with y/n input.

    Reprompt user if input is not 'y' or 'n' (case agnostic).
    Return boolean value.
    """
    while True:
        user_response = input("\nWould you like to print another "
                            "box? (y/n): ")
        if user_response.lower() == "n":
            return False
        elif user_response.lower() != "y":
            print("Sorry, didn't get that - please respond with "
                "'y' or 'n'.")
        else:
            return True


main()