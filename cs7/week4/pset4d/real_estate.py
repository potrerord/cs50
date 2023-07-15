"""Real estate agent advertisements frequently contain words from which
all vowels — except for an initial one — have been removed. Thus,

     Desirable unfurnished flat in quiet residential area

might become

    Dsrbl unfrnshd flt in qt rsdntl ar

Write a complete Python program that reads in a normal one-line
description of a property and prints the corresponding advertisement.
Your program must implement a function

def devowel(ad):
    ...
which takes the string description and returns the corresponding
vowelless ad as a string. It must also implement and use a function

def is_vowel(c): ...
that returns True if a character is vowel, a, e, i, o, u, A, E, I, O, U.
You may assume that y is not a vowel."""


def main():
    """butt"""

    print()

    print("  TEST: Desirable unfurnished flat in quiet residential area")
    print("  GOAL: Dsrbl unfrnshd flt in qt rsdntl ar\n")
    print("RESULT: ", end="")

    # Take user input.
    #########################user_ad = input("Enter ad text: ")

    user_ad = "Desirable unfurnished flat in quiet residential area"

    # Print the devoweled version of user input.
    print(devowel(user_ad))

    print()


def is_vowel(c: str) -> bool:
    """Return True if c is vowel (case insensitive)."""

    # Constant reference list for single lowercase vowel characters.
    # Note that 'y' is not considered a vowel in this program.
    LOWER_VOWELS = ['a', 'e', 'i', 'o', 'u']

    # Convert c to lowercase for comparison, return True if vowel.
    if c.lower() in LOWER_VOWELS:
        return True

    # Else, return False.
    return False


def devowel(ad: str) -> str:
    """Take the text ad and return a string with non-initial vowels
    removed.
    """

    result = ""

    for c in ad:
        if 
        elif not(is_vowel(c)):
            result += c

    return result


if __name__ == "__main__":
    main()
