"""
Reads a normal one-line description of a property and prints a "real-
estate-style" advertisement with all non-inital vowels removed.
"""


def main():
    """butt"""

    print()

    # Take user input.
    user_ad = input("Enter ad: ")

    # Print the devoweled version of user input.
    print(f"  Result: {devowel(user_ad)}")

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

    # Separate words in ad.
    words = ad.split()

    # Initialize empty result string.
    result = ""

    # Iterate through each word.
    for word in words:

        # Keep the first letter of every word.
        result += word[0]

        # Drop the non-vowels in the rest of the word.
        for c in word[1:]:
            if not(is_vowel(c)):
                result += c

        # Add a space after each word except the last.
        if word != words[-1]:
            result += " "

    return result


if __name__ == "__main__":
    main()
