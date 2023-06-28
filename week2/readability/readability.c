// Prints the Coleman-Liau index reading grade level for input text

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Prompt user for string "Text: "
    string text = get_string("Text: ");

    // a sentence is a .?! followed by a space or \0 (!!! for example should be one sentence)

    // the text is a string filled with useful spaces
    // count variables: letters, words, sentences
    int letcount = 0;
    int wordcount = 0;
    int sentcount = 0;

    // Scan all characters in string
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        // If char is alpha, count letter

        if (isalpha(text[i]) != 0)
        {
            letcount++;
        }

        // If char is not alpha
        else
        {
            // Apostrophe special case: only plural possessive ends word
            if (text[i] == '\'')
            {
                if (isalpha(text[i - 1]) != 0 && isalpha(text[i + 1] == 0))
                {
                    wordcount++;
                }
            }

            // Ignore hyphens
            else if (text[i] != '-')
            {
                // If previous char is alpha count word
                if (isalpha(text[i - 1]) != 0)
                wordcount++;
            }
        }

        // if it's an apostrophe in between two alphas then ignore, if it's an apostrophe at the end of a word then that's a word then move on without doing anything

        // Count sentences
        // when you reach a .?! + ' ' or '\0' it's a sentence
        // if it's whitespace or null

        if (isspace(c) != 0 || c == '\0')
        {

        }

        // if it is a .?!, check the character after it
            // if the next character is a space or \0, that's a sentence buddy count it in sentence counter
        // if that counter is a nonzero positive integer, increment a "letters" sum with it
            // increment a "words" sum by 1 when this happens

    }

    // Calculate Coleman-Liau index = (0.0588 * L) - (0.296 * S) - 15.8
    // L = average number of letters per 100 words in the text (more letters brings level up)
        // get number of letters for every 100 groups of alpha
        // A word could be defined as connected alpha characters and apostrophes, ignoring punctuation and separated by spaces
            // Anthony's is one word
            // Anthony. is a word not including the period
            // let's just ignore punct and use spaces to indicate new word
        // float letters / float words / 100 = average letters / 100 words
        // in each

    // S = average number of sentences per 100 words in the text (more sentences brings level down)
    // float sentences / float words / 100 = average sentences / 100 words


    // Print "Grade X"
    // if < 1 print "Before Grade 1"
    // if >= 16 print "Grade 16+"
}