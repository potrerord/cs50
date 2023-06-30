"""Takes your order."""

NAME = "Devon"


def main():
    print(f"Hi, {NAME}!")
    order = get_size("What would you like to order? ")


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
