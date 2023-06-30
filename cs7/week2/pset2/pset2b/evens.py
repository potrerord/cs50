"""
Outputs the sum of all even integers from 2 up to and including an
integer provided by the user.
"""

def main():
    """Take user input for upper inclusive limit of even integer
    sequence and print sum.
    """

    n = int(input("I will compute the sum of even integers from "
                  "2 through? "))
    sum = 0

    for even in range(2, n + 1, 2):
        sum += even

    print("The sum is", sum)