// Prints the Coleman-Liau index reading grade level for input text

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Prompt user for string "Text: "
    string input_text = get_string("Text: ");
    const int N = strlen(input_text);
    string text[N + 1] = input_text;
    text[N] = ' ';
    printf("%s.", text);

    // add a space after the last word manually so it'll be easier for the program to distinguish sentences (!!! for example should be one sentence)

    // the text is a string filled with useful spaces
    // for every character in the string,
    // if it's not a space, period, question mark, or exclamation point, count it - when you reach a space, that count is the letters in that word
    // if that counter is a nonzero positive integer, increment a "letters" sum with it
        // increment a "words" sum by 1 when this happens


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