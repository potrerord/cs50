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

    # Initialize letters set (layout recommended by style50).
    letters_set = {
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    }

    # Remove all matches.
    for word in word_list:
        for char in word:
            letters_set.discard(char.upper())

    # Create sorted list of remaining letters.
    remaining_letters = sorted(list(letters_set))

    return remaining_letters


if __name__ == "__main__":
    main()
