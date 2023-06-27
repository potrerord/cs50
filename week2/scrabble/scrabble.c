// Takes 2 Scrabble word inputs, compares Player 1 to Player 2 and prints win result

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

// Scrabble letter values alpha order
const int SCRABVAL = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10}

// Gets scrabble score of input alpha characters
int scrabble_score(string s);

int main(void)
{
    // Create array of letter scores


    // Prompt Player 1
    string p1 = get_string("Player 1: ");

    // Prompt Player 2
    string p2 = get_string("Player 2: ");

    // Put player words in array


    // Get each score
    int p1score = scrabble_score(p1);
    int p2score = 0;

    // Print winner
    if (p1score > p2score)
    {
        printf("Player 1 wins!\n");
    }
    else if (p1score < p2score)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

// Gets scrabble score of input alpha characters
int scrabble_score(string s)
{
    // Initialize final and letter-by-letter score variables, plus char x variable for s[i] to avoid changing str data
    int sum = 0;
    int letter = 0;
    char x;

    // For every character in s
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        // Char variable x for s[i] to avoid changing string data
        x = s[i];

        // If x is alpha
        if (isalpha(x) != 0)
        {
            // Convert x to uppercase if necessary
            if (isupper(x) == 0)
            {
                x = toupper(x);
            }

            // Check against the all-uppercase score key
            // letter = whatever the score key says for that letter

            sum += letter;
        }
    }
    return sum;
}