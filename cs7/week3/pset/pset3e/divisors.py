"""
Prints a list of positive ints within an inclusive user-input range,
designating each int as deficient, perfect, or abundant based on the sum
of its proper divisors.
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

    # Limit search for factor pairs to be <= the square root of num.
    sqrt = num ** 0.5

    # Initiate sum variable.
    sum = 0

    # If num is divisible by a number <= its square root,
    for potential_div in range(1, int(sqrt) + 1):
        if num % potential_div == 0:
            sum += potential_div

            # Avoid adding square root twice.
            if potential_div < sqrt:

                # Add the other member of the divisor's factor pair.
                sum += num / potential_div

    # Subtract num from its own sum.
    sum -= num

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
