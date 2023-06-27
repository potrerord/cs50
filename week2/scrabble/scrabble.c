// Takes 2 Scrabble word inputs, compares Player 1 to Player 2 and prints win result

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

// Scrabble letter values alpha order
const int SCRABVAL[26] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

// Number of players
const int N = 2;

// Gets scrabble score of input alpha characters
int scrabble_score(string s);

int main(void)
{
    // Create array for player inputs of size N
    string words[N] = NULL;

    // Prompt players for words and put in array
    for (i = 0; i < N; i++)
    {
        words[i] = get_string("Player %i: ", i);
    }

    // Create array for player scores
    int pscores[N] = NULL;

    // Put player scores in array
    for (i = 0; i < N; i++)
    {
        pscores[i] = scrabble_score(words[i]);
    }

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
    // Initialize final and letter-by-letter score variables, plus char x variable to store s[i]
    int sum = 0;
    int xval = 0;
    char x;

    // For every character in s
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        x = s[i];

        // If x is alpha
        if (isalpha(x) != 0)
        {
            // Convert x to uppercase if necessary
            x = toupper(s[i]);

            // Convert uppercase alpha ASCII to SCRABVAL index
            xval = SCRABVAL[x - 65];

            // Add value to summed score
            sum += xval;
        }
    }
    return sum;
}