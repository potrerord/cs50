"""
Write a Python program that prompts the user for the day and month
(both integers) of their birthday, and then prints the appropriate
astrological sign according to the following:

Aries: Mar21-Apr19
Taurus: Apr20-May20
Gemini: May21-Jun20
Cancer: Jun21-Jul22
Leo: Jul23-Aug22
Virgo: Aug23-Sep22
Libra: Sep23-Oct22
Scorpio: Oct23-Nov21
Sagittarius: Nov22-Dec21
Capricorn: Dec22-Jan19
Aquarius: Jan20-Feb18
Pisces: Feb19-Mar20

Your program must implement a function

def sign(month, day):
    ...

that takes the month and day as input and returns the sign. For example,
sign(3, 21) should return the string "Aries". Sign should return the
string "INVALID_DATE" if the date is not valid. The function sign should
not print anything out. Feb 29 is considered a valid date. To simplify
your sign function, you program must also implement function

def before(month1, day1, month2, day2):
    ...

that takes in two dates (assumed to be valid) and returns true if
month1, day1 is strictly before month2, day2 and returns false
otherwise. You must make (repeated) use of the function before in sign
to decide what the sign of the date is.
"""


#  Implement a comparison function for dates
#
#  Returns true if the date (month1, day1) is
#  earlier in the calendar than (month2, day2).
#  Assumes the days are valid and doens't do any checking.



def main():
    """Prompt the user for a month and day, then print the return of
    sign function.
    """

    print()
    month = int(input("Enter a month (integer): "))
    day = int(input("Enter a day (integer): "))
    print(f"Your chosen date is {month}/{day}.")
    print()
    print(sign(month, day))


def before(month1, day1, month2, day2) -> bool:
    """Return true if month1/day1 is before month2/day2."""

    # If month1 is after month2, immediately return False.
    if month1 > month2:
        return False

    # If month1 is before month2, immediately return True.
    elif month1 < month2:
        return True

    # If months are equal, check days.
    else:

        # If day1 is before day2, return True.
        if day1 < day2:
            return True

        # If day1 is not strictly before day2, return False.
        else:
            return False


def sign(month, day) -> str:
    """Return the sign for the given month and day, or "INVALID_DATE" if
    the date is not valid.
    """

    


# Run the main function if script is run directly.
if __name__ == "__main__":
    main()
