"""
Prints 5-digit number that matches its reverse when multiplied by four.
"""


def main():
    """Call five_digits() and print result."""

    print()
    print(five_digits())
    print()


def five_digits():
    """Find and return 5-digit integer that when multiplied by 4 matches
    its reverse.
    """
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


# Run the main function if script is run directly.
if __name__ == "__main__":
    main()

