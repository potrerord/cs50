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
    """Call five_digits() and print result.
    """
    print(five_digits())


# Finds and returns the 5-digit number that when multiplied by 4 is the
# original number with the digits reversed.
#
# Must not print anything out.
def five_digits():
    for number in range(1000, 10000):
        ones = number % 10
        tens = (number / 10) % 10
        hund = (number / 100) % 10
        thou = (number / 1000) % 10

        conv_ones = thou
        conv_tens = hund * 10
        conv_hund = tens * 100
        conv_thou = ones * 1000

        conv_number = conv_thou + conv_hund + conv_tens + conv_ones

        if number * 4 == conv_number:
            return number

# Runs the main function. Leave as is.
if __name__ == "__main__":
    main()

