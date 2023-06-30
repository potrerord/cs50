"""Takes your order."""

NAME = "Devon"

def main():
    print("Hello, {NAME
    order = get_order("What would you like to order? ")



def get_order(prompt: str) -> str:
    """Prompt user and continually reprompt if input is not alpha.
    Return string user input.

    Keyword argument:
    prompt -- The string prompt that will accept user input.
    """

    while True:
        user_input = input("\n" + prompt)
        if user_input.isdigit():
            return float(user_input)
        print("error: temperature must be numeric")


def get_name(prompt: str) -> float:
    """Prompt user and continually reprompt if input is alpha.
    Return float user input.

    Keyword argument:
    prompt -- The string prompt that will accept user input.
    """

    while True:
        user_input = input("\n" + prompt)
        if user_input.isdigit():
            return float(user_input)
        print("error: temperature must be numeric")


main()
