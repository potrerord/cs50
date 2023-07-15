"""
Prints a list of strings with each letter of each string sorted in case-
insensitive alphabetical order.
"""


from typing import List


def main():
    """Call alphabetical with test values."""

    # Constant test value.
    TEST = ['apple', 'pumpkin', 'log', 'River', 'fox', 'pond']

    # Get user input (test value currently).
    user_list = TEST

    # Print result.
    print()
    print(alphabetical(user_list))
    print()


def alphabetical(words: List[str]) -> List[str]:
    """Return a converted list of words with each letter of each word
    sorted in alphabetical order, preserving case.
    """

    # Initialize empty sorted list.
    sorted_words = []

    # Iterate through every word in the argument list.
    for word in words:
        # Convert word to list.
        list_word = list(word)

        # Sort list case-insensitively.
        sorted_list = sorted(list_word, key=str.lower)

        # Convert list to string.
        sorted_word = "".join(sorted_list)

        # Add string to sorted_words list.
        sorted_words.append(sorted_word)

    return sorted_words


if __name__ == "__main__":
    main()
