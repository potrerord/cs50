"""
Prints the Coleman-Liau index reading grade level for input text.
"""


def main():
    """Print grade level for input text."""

    # Prompt user for text to analyze
    s = input("Enter text: ")

    # Initiate counter variables.
    letters = 0
    words = 0
    sentences = 0

    # Scan each character in string to count letters/words/sentences.
    for char in s:
        if char.isalpha():
            letters += 1
        elif char.isspace():
            words += 1
        elif char in {".", "!", "?"}:
            sentences += 1

    # Store rounded Coleman-Liau index
    level = round(cole_liau(letters, words, sentences))

    # Print Grade X
    if level < 1:
        print("Before Grade 1.")
    elif level > 15:
        print("Grade 16+")
    else:
        for grade in range(1, 16):
            if grade == level:
                print("Grade {level}")


def cole_liau(letters: int, words: int, sentences: int) -> float:
    """Return the Coleman-Liau index given the arguments."""

    score = (
        (0.0588 * letters / (100 * words)) - (0.296 * sentences / (100 * words)) - 15.8
    )

    return score


if __name__ == "__main__":
    main()
