"""
Prints an alphabetized list of letters not used by a particular list of
words.
"""


def main():
    """Test function."""

    test_list = ["Now", "is", "the", "TIME"]
    print(missing_letters(test_list))


def missing_letters(word_list):
    """Take a word list and return a sorted list of capitalized letters
    that do not appear in the list.
    """

    # Initialize letters list.
    letters = ['A', 'B', 'C', 'D', 'E', 'F',
               'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X',
               'Y', 'Z']

    # Remove all matches.
    for word in word_list:
        for char in word:
            letters.discard(char.upper())

    return letters


if __name__ == "__main__":
    main()
