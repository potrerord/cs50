"""
Prints the Coleman-Liau index reading grade level for input text.
"""


def main():
{
    """butt"""

    # Prompt user for text to analyze
    s = input("Enter text: ")

    # Declare count variables for input text: letters, words, sentences.
    

    # Scan each character in string
        # If char is alpha, count letter

        # If char is not alpha check if it ends word

"""Problem spec says to assume a word is a sequence of chars separated
by a space. You should just be counting spaces here, you don't need to
have all of these complex checks.
"""

"""
This condition is not necessary, just count the periods, exclamations
and question marks.
"""

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
