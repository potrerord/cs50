#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <strings.h>

// Max voters and candidates
#define MAX_VOTERS 100
#define MAX_CANDIDATES 9

// preferences[i][j] is jth preference for voter i
int preferences[MAX_VOTERS][MAX_CANDIDATES];

// Candidates have name, vote count, eliminated status
typedef struct
{
    string name;
    int votes;
    bool eliminated;
}
candidate;

// Array of candidates
candidate candidates[MAX_CANDIDATES];

// Numbers of voters and candidates
int voter_count;
int candidate_count;

// Function prototypes
bool vote(int voter, int rank, string name);
void tabulate(void);
bool print_winner(void);
int find_min(void);
bool is_tie(int min);
void eliminate(int min);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: runoff [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX_CANDIDATES)
    {
        printf("Maximum number of candidates is %i\n", MAX_CANDIDATES);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
        candidates[i].eliminated = false;
    }

    voter_count = get_int("Number of voters: ");
    if (voter_count > MAX_VOTERS)
    {
        printf("Maximum number of voters is %i\n", MAX_VOTERS);
        return 3;
    }

    // Keep querying for votes
    for (int i = 0; i < voter_count; i++)
    {

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            // Record vote, unless it's invalid
            if (!vote(i, j, name))
            {
                printf("Invalid vote.\n");
                return 4;
            }
        }

        printf("\n");
    }

    // Keep holding runoffs until winner exists
    while (true)
    {
        // Calculate votes given remaining candidates
        tabulate();

        // Check if election has been won
        bool won = print_winner();
        if (won)
        {
            break;
        }

        // Eliminate last-place candidates
        int min = find_min();
        bool tie = is_tie(min);

        // If tie, everyone wins
        if (tie)
        {
            for (int i = 0; i < candidate_count; i++)
            {
                if (!candidates[i].eliminated)
                {
                    printf("%s\n", candidates[i].name);
                }
            }
            break;
        }

        // Eliminate anyone with minimum number of votes
        eliminate(min);

        // Reset vote counts back to zero
        for (int i = 0; i < candidate_count; i++)
        {
            candidates[i].votes = 0;
        }
    }
    return 0;
}


// Record preference if vote is valid
bool vote(int voter, int rank, string name)
{

    // Iterate over every candidate and check for match between vote/
    // candidate name. Ignores case.
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcasecmp(name, candidates[i].name) == 0)
        {
            // Log candidate with voter and ranking, then return true to
            // indicate successful vote. Note: logs candidate with no
            // case changes after case-insensitively checking for valid
            // vote, so future checks will also need to ignore case.
            preferences[voter][rank] = name;
            return true;
        }

    // Return false to indicate vote that does not match candidate.
    return false;
}


// Tabulate votes for non-eliminated candidates.
void tabulate(void)
{
    // Initiate variable to track if top valid preference was
    // successfully counted, like a function return value.
    bool vote_counted = false;

    // Iterate through each voter.
    for (int i = 0; i < voter_count; i++)
    {

        // Reset vote_counted status.
        vote_counted = false;

        // Iterate through voter preferences.
        for (int j = 0; j < candidate_count; j++)
        {

            // Iterate through candidate list.
            for (int k = 0; k < candidate_count; k++)
            {

                // If candidate is not eliminated and is a case-
                // insensitive match with voter preference, then
                // increment candidate's vote count. Break after first
                // non-eliminated preference per voter.
                if (strcasecmp(preferences[i][k], candidates[j]) == 0 &&
                    !candidates[k].eliminated)
                {
                    candidates[k].votes++;
                    vote_counted = true;
                    break
                }
            }

            // Move onto next voter if top preference was successfully
            // counted, otherwise check next preference.
            if (vote_counted == true)
            {
                break
            }
        }
        preferences[i]
    }

    // Iterate through every non-eliminated candidate
    for (int i = 0; i < candidate_count; i++)
    {
        if (!candidate[i].eliminated)
        {

        }
    }
    return;
}


// Print the winner of the election, if there is one
bool print_winner(void)
{
    // TODO
    return false;
}


// Return the minimum number of votes any remaining candidate has
int find_min(void)
{
    // TODO
    return 0;
}


// Return true if the election is tied between all candidates, false otherwise
bool is_tie(int min)
{
    // TODO
    return false;
}


// Eliminate the candidate (or candidates) in last place
void eliminate(int min)
{
    // TODO
    return;
}