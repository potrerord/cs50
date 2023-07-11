"""
Prints the Coleman-Liau index reading grade level for input text.
"""


def main():

    """butt"""

    # Prompt user for text to analyze
    s = input("Enter text: ")

    # Scan each character in string to count letters/words/sentences.
    for char in s:
        if char.isalpha():
            letters += 1
        elif char.isspace():
            words += 1
        elif char in {'.', '!', '?'}:
            sentences += 1

    # Store rounded Coleman-Liau index
    int gradeLevel = round(cole_liau(letCount, wordCount, sentCount));

    # Print Grade X


"""
Calculates Coleman-Liau index = (0.0588 * let/100words) - (0.296 * sent/100words) - 15.8
Better to use the actual formula here, as it makes this line easier to understand.
"""

float cole_liau(int lets, int wrds, int snts)
{
    float score = (05.88 * lets / wrds) - (29.6 * snts / wrds) - 15.8;
    return score;
}


if __name__ == "__main__":
    main()
