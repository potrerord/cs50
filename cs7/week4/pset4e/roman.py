"""
Write a program to read in a string of characters that represent a Roman
numeral and then convert it to Arabic form (an integer). The character
values for Roman numerals are as follows:

Symbol  Value
M       1000
D       500
C       100
L       50
X       10
V       5
I       1

You may assume that the user inputs a valid Roman numeral representing a
value between 1 and 3999. Test your program with the following data:

LXXXVII (87)
CCXIX (219)
MCCCLIV (1354)
MMDCLXXIII (2673)
MCDLXXVI (1476)

For your reference, the following link has a chart of many Roman
numerals: http://literacy.kent.edu/Minigrants/Cinci/romanchart.htm

You must define a function

def to_arabic(roman_numeral):
    ...

that takes a valid Roman numeral and converts it to the corresponding
decimal number.

5 points bonus Extra Credit
Extend your Roman numerals solutions to print an error if an invalid
Roman numeral is input. A numeral could be invalid because it includes
invalid characters, such as A, B, or is lowercase. In addition, numerals
like IXI, VC, and XVIIIII that have too many symbols or symbols in the
wrong order are also invalid. The form XXXXVIIII is also considered
invalid for this problem. Your program should reject all invalid Roman
numerals, including ones with the wrong order or too many symbols.

You must define a function
def is valid(roman_numeral):
    ...

that takes a Roman numeral and returns True if it is valid and False if
it is not.
"""


def main():
    # Add your solution to the problem that makes use of the above.
    print("Implement me!")


def to_arabic(roman_numeral):
    """Takes a valid roman numeral and returns an integer that is
    the corresponding the decimal number"""
    # Add your code here.


def is_valid(roman_numeral):
    """Bonus EC problem: takes a roman numeral and returns a boolean
    that is True if the numeral is valid and False if it is not"""
    # Add your code here.


if __name__ == "__main__":
    main()
