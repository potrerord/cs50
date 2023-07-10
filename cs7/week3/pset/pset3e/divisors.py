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
        print(f"{i} is {divisors(i)}.")


def divisors(num):
    """Return "deficient", "perfect", or "abundant" for an integer n."""

    # Special case: 1 is not a perfect number.
    if num == 1:
        return False

    # Limit search for factor pairs to be <= the square root of num.
    factor_ceil = int(num ** 0.5)

    # Initiate sum variable at 1 to skip first factor pair.
    sum = 1

    # If num is divisible by a number <= its square root,
    for potential_div in range(2, factor_ceil + 1):
        if num % potential_div == 0:
            sum += potential_div

            # Avoid adding square root twice.
            if potential_div < factor_ceil:

                # Add the other member of the divisor's factor pair.
                sum += num / potential_div

    # Classify number according to the sum of its divisors.
    if sum < num:
        return "deficient"
    elif sum > num:
        return "abundant"
    else:
        return "perfect"


# Runs the main function. Leave as is.
if __name__ == "__main__":
    main()
