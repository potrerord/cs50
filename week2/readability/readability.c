// Prints the Coleman-Liau index reading grade level for input text

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

// Calculates Coleman-Liau index = (0.0588 * let/100words) - (0.296 * sent/100words) - 15.8
float cole_liau(int lets, int wrds, int snts);

int main(void)
{
    // Prompt user for string "Text: "
    string text = get_string("Text: ");

    // a sentence is a .?! followed by a space or \0 (!!! for example should be one sentence)

    // the text is a string filled with useful spaces
    // count variables: letters, words, sentences
    int letCount = 0;
    int wordCount = 0;
    int sentCount = 0;

    // Scan all characters in string
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        // If char is alpha, count letter

        if (isalpha(text[i]) != 0)
        {
            letCount++;
        }

        // If char is not alpha
        else
        {
            // Apostrophe special case: only plural possessive ends word
            if (text[i] == '\'')
            {
                if (isalpha(text[i - 1]) != 0 && isalpha(text[i + 1] == 0))
                {
                    wordCount++;
                }
            }

            // Ignore hyphens
            else if (text[i] != '-')
            {
                // If previous char is alpha count word
                if (isalpha(text[i - 1]) != 0)
                wordCount++;

                // If sentence-ending punctuation followed by space or null, count sentence
                if (text[i] == '.' || text[i] == '?' || text[i] == '!')
                {
                    if (isspace(text[i + 1]) != 0 || text[i + 1] == '\0')
                    {
                        sentCount++;
                    }
                }
            }
        }
    }

    // Calculate Coleman-Liau index = (0.0588 * L) - (0.296 * S) - 15.8
    float gradeLevel = cole_liau(letCount, wordCount, sentCount);

    // Print "Grade X"
    // if < 1 print "Before Grade 1"
    if (gradeLevel < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (gradeLevel >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", (int)gradeLevel);
    }
}

// Calculates Coleman-Liau index = (0.0588 * let/100words) - (0.296 * sent/100words) - 15.8
float cole_liau(int lets, int wrds, int snts)
{
    float score = (05.88 * lets / wrds) - (29.6 * snts / wrds) - 15.8;
    return score;
}