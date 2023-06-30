"""
Outputs the sum of all even integers from 2 up to and including an
integer provided by the user.
"""

def main():
    """Take user input for upper inclusive limit of even integer
    sequence and print sum.
    """

    n = get_range()



    print("The sum is", sum)


def get_range() -> int:
    """Prompt user and continually reprompt if input is not a positive
    integer greater than 2. Return integer input.
    """

    while True:
        user_input = input("\nI will compute the sum of even integers "
                           "from 2 through? ")
        if user_input.isdigit() and int(user_input) > 0:
            return int(user_input)
        print("Size must be a positive integer greater than 2.")


def sum_evens(start: int, stop: int) -> int:
    """Calculate and return the integer sum of all positive even
    integers in a range.

    Keyword arguments:
    start -- inclusive lower bound
    stop -- exclusive upper bound, a la range()
    """

    sum = 0
    for even in range(lower, upper, 2):
        sum += even
    return sum