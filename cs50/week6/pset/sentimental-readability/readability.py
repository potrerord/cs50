"""
Prints the Coleman-Liau index reading grade level for input text.
"""

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
Instructor
| 07/02 at 10:59 am
Grading comment:
Problem spec says to assume a word is a sequence of chars separated by a space. You should just be counting spaces here, you don't need to have all of these complex checks.

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
Instructor
| 07/02 at 11:01 am
Grading comment:
This condition is not necessary, just count the periods, exclamations and question marks.

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
Instructor
| 07/02 at 11:02 am
Grading comment:
Better to use the actual formula here, as it makes this line easier to understand.

    return score;
}
