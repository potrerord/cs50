"""
Prompts the user for an integer and prints all perfect numbers up to
that integer.
"""


def main():
    user_int = int(input("Enter an integer: "))
    # For every int up to and including the input

    for i in range(user_int + 1):
        if is_perfect_number(i):
            print(i)

def is_perfect_number(test_int) -> bool:
    """Return true if test_int is a perfect number.

    An integer is perfect if it is equal to the sum of its divisors,
    except itself.
    """


    # Store the square root of test_int (the square root of an integer
    # is the upper limit for where you'll stop finding new factor
    # pairs).
    sqrt = test_int ** 0.5

    # Initiate sum variable at 1 to skip first factor pair, which would
    # contain test_int, which should not be included in the sum.
    sum = 1

    # If user_int is divisible by a number <= its square root,
    for checked_divisor in range(2, sqrt_user_int + 1):
        if num % checked_divisor == 0:
            sum += checked_divisor

            # Avoid adding sqrt twice, avoid adding self at all.
            if

            if checked_divisor < sqrt_user_int:

                # Add the other member of the divisor's factor pair.
                sum += user_int / checked_divisor

    if




main()