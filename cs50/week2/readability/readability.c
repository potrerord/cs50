// Prints the Coleman-Liau index reading grade level for input text

#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

// Calculates Coleman-Liau index given # of letters, words, and sentences
float cole_liau(int lets, int wrds, int snts);

int main(void)
{
    // Prompt user for text to analyze
    string text = get_string("Text: ");

    // Declare count variables for input text: letters, words, sentences
    int letCount = 0;
    int wordCount = 0;
    int sentCount = 0;

    // Scan each character in string
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        // If char is alpha, count letter
        if (isalpha(text[i]) != 0)
        {
            letCount++;
        }

        // If char is not alpha check if it ends word
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
                {
                    wordCount++;
                }

                // If nonalpha char is .?! followed by space or null, count sentence
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

    // Store rounded Coleman-Liau index
    int gradeLevel = round(cole_liau(letCount, wordCount, sentCount));

    // Print Grade X
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
        printf("Grade %i\n", gradeLevel);
    }
}

// Calculates Coleman-Liau index = (0.0588 * let/100words) - (0.296 * sent/100words) - 15.8
float cole_liau(int lets, int wrds, int snts)
{
    float score = (05.88 * lets / wrds) - (29.6 * snts / wrds) - 15.8;
    return score;
}