"""
Prints a box with user-input size.
Example of size 3: +--+
                   |  |
                   +--+
"""


def main():
    """Prompts user for positive int and runs draw_box function."""

    # Setup for end-of-program "again?" prompt.
    while True:

        # Gets positive integer size from user.
        user_size = get_size()

        # Draws box after a new line.
        print()
        draw_box(user_size)

        # Asks user if they would like to run program again.
        

        while True:
            user_redo = input("\nWould you like to print another "
                              "box? (y/n): ")
            if user_redo.lower() == "n":
                print()
                return
            elif user_redo.lower() != "y":
                print("Sorry, didn't get that - please respond with "
                    "'y' or 'n'.")
            else:
                pass


def get_size() -> int:
    """Continually reprompts user for size if input is not pos int."""

    while True:
        user_input = input("\nEnter a size: ")
        if user_input.isdigit() and int(user_input) > 0:
            return int(user_input)
        print("Size must be a positive integer.")


def draw_box(size: int):
    """Takes integer argument and draws argument-sized box."""

    # Size of 1 is special case, just prints a +.
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

            # Prints end, middle, end for each row. Middle is reduced by 2
            # to account for end characters.
            print(end_char + mid_char * (size - 2) + end_char)


main()