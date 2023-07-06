"""Takes your order."""

NAME = "Devon"


def main():
    print(f"Hi, {NAME}!")

    # Get order until customer stops.
    while True:
        order = get_alpha("What would you like to order? ")

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


main()
