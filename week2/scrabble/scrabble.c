// Takes 2 Scrabble word inputs, compares Player 1 to Player 2 and prints win result

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

// Scrabble letter values alpha order
const int SCRABVAL[26] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

// Number of players
const int N = 3;

// Returns 1 if all values are equal, 0 if any are different (requires an array input with null final value)
int is_tie(int scores[]);

// Gets scrabble score of input alpha characters
int scrabble_score(string s);

int main(void)
{
    // Create array for player inputs
    string words[N];
    for (int i = 0; i < N; i++)
    {
        words[i] = get_string("Player %i: ", i + 1);
    }

    // Create array for player scores with null value at the end
    int pscores[N + 1];
    for (int i = 0; i < N; i++)
    {
        pscores[i] = scrabble_score(words[i]);
    }
    pscores[N] = '\0';

    // Check for tie and print if found
    if (is_tie(pscores) == 1)
    {
        printf("Tie!\n");
    }

    // Else, find winner
    else
    {
        int winner = 0;
        for (int i = 0; i < N; i++)
        {
            if (pscores[i] > winner)
            {
                winner = i + 1;
            }
        }

        // Print winner
        printf("Player %i wins!\n", winner);
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

// Returns 1 if all values are equal, 0 if any are different (requires an array input with null final value)
int is_tie(int scores[])
{
    // if all are equal return 1
    int i = 1;
    while (1 == 1)
    {
        // Return 1 if all scores are the same
        if (scores[i] == '\0')
        {
            return 1;
            break;
        }

        // Return 0 is any score is different
        else if (scores[i] != scores[i - 1])
        {
            return 0;
            break;
        }

        // Increment
        i++;
    }
}
