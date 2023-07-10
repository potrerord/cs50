"""
The proper divisors of an integer n are the positive divisors less than
n. A positive integer is said to be a deficient, perfect, or abundant
number if the sum of its proper divisors is less than, equal to, or
greater than the number, respectively.

For example,
8 is deficient,
    because its proper divisors are 1, 2 and 4, and 1+2+4 < 8;
6 is perfect,
    because 1+2+3 = 6;
12 is abundant,
    because 1+2+3+4+6 > 12.

Write a Python program that accepts two positive integer values that are
input by the user running the program (say m and n, where m <= n) and
prints deficient, perfect or abundant for each value between m and n
inclusive. Your program must implement a function

def divisors(n):
    ...

The function must return (not print!) deficient, perfect or abundant for
a given number. You may want to Google for examples of perfect numbers
to be sure your function is behaving correctly. The output from your
main program will look something like this:

Please input an integer value for m: 5
Now input an integer value for n that is greater than or equal to 5: 31
   5 is deficient
   6 is perfect
   7 is deficient
...

"""


def main():
    """Prompt the user for two numbers and call divisors."""

    # Prompt user for range.
    start = int(input("Enter start value: "))
    end = int(input("Enter end value:   "))

    # Iterate up to and including end value.
    for i in range(start, end + 1):
        divisors(i)


def divisors(n):
    """Return "deficient", "perfect", or "abundant" for an integer n."""


def is_perfect_number(num) -> bool:
    """Return true if test_int is a perfect number.

    An integer is perfect if it is equal to the sum of its divisors,
    except itself.
    """

    # Special case: 1 is not a perfect number.
    if num == 1:
        return False

    # Limit the search for factor pairs at the square root of num.
    sqrt = num ** 0.5

    # Initiate sum variable at 1 to skip first factor pair.
    sum = 1

    # If num is divisible by a number <= its square root,
    for poss_divisor in range(2, int(num ** 0.5) + 1):
        if num % poss_divisor == 0:
            sum += poss_divisor

            # Avoid adding square root twice.
            if poss_divisor < sqrt:

                # Add the other member of the divisor's factor pair.
                sum += num / poss_divisor

    # Return true if test_int is a perfect number.
    if num == sum:
        return True

    # Return false if not.
    return False





# Runs the main function. Leave as is.
if __name__ == "__main__":
    main()
