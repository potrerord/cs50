"""
Prompts the user for an integer and prints all perfect numbers up to
that integer.
"""


def main():
    user_int = int(input("Enter an integer: "))
    # For every int up to and including the input

    for i in range(1, user_int + 1):

    # Store the square root of the int (the square root of an integer is
    # the upper limit for where you'll stop finding new factor pairs).
    sqrt_user_int = user_int ** 0.5

    # Initiate sum variable.
    sum = 0

    # If user_int is divisible by a number <= its square root,
    for i in range(1, sqrt_user_int + 1):
        if user_int % i == 0:
            sum += i

            if i == sqrt_user_int
            sum += user_int / i




main()