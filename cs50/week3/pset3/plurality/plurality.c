#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
}
candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }

    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    // Display winner of election
    print_winner();
}

// Update vote totals given a new vote
bool vote(string name)
{
    // Iterate over every candidate.
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(tolower(name), tolower(candidates[i].name)) == 0)
        {
            // Increment candidate's vote count and return true to
            // indicate successful vote.
            candidates[i].votes++;
            return true;
        }
    }

    // Return false to indicate vote that does not match candidate.
    return false;
}

// Print the winner (or winners) of the election
void print_winner(void)
{
    // TODO
    string winners[MAX + 1] = {NULL};
    string current_winner = {NULL};
    int current_win_votes = -1;

    for (int i = 0; i < candidate_count; i++)
    {
        // Fill "winners[]" array with names of winner(s_ to account for
        // unlikely maximum tie between all candidates. winners[] begins
        // assigning at winners[1] to avoid breaking the "erase previous
        // winner's name" rule for the first candidate.
        if (candidates[i].votes > win_votes)
        {
            // Add current lead to winners[].
            winners[i + 1] = candidates[i].name;

            // Erase previous winner's name.
            winners[i] = {NULL};
            current_winner = candidates[i].name;
            win_votes = candidates[i].votes;
        }
        else if (candidates[i].votes == win_votes)
        {

        }
    }

    // If a tie, print all tied names

    return;
}