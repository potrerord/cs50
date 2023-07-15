"""
Define a function named alphabetical that accepts a list of words as its
only parameter and constructs/returns a list of strings with each
of the letters in each word sorted in alphabetical, not unicode, order.

For example, the call alphabetical(['apple', 'pumpkin', 'log', 'River',
'fox', 'pond']) should return the list ['aelpp', 'ikmnppu', 'glo',
'eiRrv', 'fox', 'dnop'].
"""


from typing import List


def main():
    """Call alphabetical."""

    test = ['apple', 'pumpkin', 'log', 'River', 'fox', 'pond']

    print()
    print("TEST: ['apple', 'pumpkin', 'log', 'River', 'fox', 'pond']")
    print("GOAL: ['aelpp', 'ikmnppu', 'glo', 'eiRrv', 'fox', 'dnop']")
    print(f"REAL: {alphabetical(test)}")
    print()


def alphabetical(words: List[str]) -> List[str]:
    """Return a converted list of words with each letter of each word
    sorted in alphabetical order, preserving case.
    """

    # Initialize empty sorted list.
    sorted_words = []

    # Iterate through every word in the argument list.
    for word in words:
        sorted_word = list(word).sort()
        sorted_words.append(sorted_word)

    return sorted_words

if __name__ == "__main__":
    main()
