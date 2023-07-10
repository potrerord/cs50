"""
If you take the number 2178, multiply it by four, and reverse the digits
— you will get 2178 again. This is the only four-digit number that has
this property. There is also a five- digit number that has the same
property. Write a program to find it! Note: you may not use any
functions we haven't yet covered, such as reversed(). As well, you
cannot use any strings to solve this.

Your program must implement a function
   def five_digits():
       ...

that finds and returns (and doesn't print!) the number.
"""


# Add a main function that calls five_digits and prints out the
# results of five_digits.
def main():
    """Call five_digits() and print result."""

    print()
    print(five_digits())
    print()


# Finds and returns the 5-digit number that when multiplied by 4 is the
# original number with the digits reversed.
#
# Must not print anything out.
def five_digits():
    for num in range(10000, 100000):
        ones = num % 10
        tens = int(num / 10) % 10
        hund = int(num / 100) % 10
        thou = int(num / 1000) % 10
        tenthou = int(num / 10000) % 10

        rev_ones = tenthou
        rev_tens = thou * 10
        rev_hund = hund * 100
        rev_thou = tens * 1000
        rev_tenthou = ones * 10000

        rev_num = rev_tenthou + rev_thou + rev_hund + rev_tens + rev_ones

        if num * 4 == rev_num:
            return num

# Runs the main function. Leave as is.
if __name__ == "__main__":
    main()

