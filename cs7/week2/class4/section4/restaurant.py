"""Takes your order."""

NAME = "Devon"


def main():
    print(f"Hi, {NAME}!")

    # Ask user if they would like to run program again, then loop
        # accordingly.
        user_redo = get_redo()
        if user_redo == False:
            print()
            return
        else:
            pass
    while True:
        order = get_size("What would you like to order? ")
        "Would you like to add another item? (y/n)"

    # Did you mean _________?


def get_alpha(prompt: str) -> str:
    """Prompt user and continually reprompt if input is not alpha.
    Return string user input.

    Keyword argument:
    prompt -- The string prompt that will accept user input.
    """

    while True:
        user_input = input("\n" + prompt)
        if user_input.isalpha():
            return float(user_input)
        print("I'm sorry, I didn't quite get that.")


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
