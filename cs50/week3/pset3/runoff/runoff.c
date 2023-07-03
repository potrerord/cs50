#include <cs50.h>
#include <stdio.h>
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
            // Log candidate index with voter and ranking, then return
            // true to indicate successful vote.
            preferences[voter][rank] = i;
            return true;
        }
    }

    // Return false to indicate vote that does not match valid
    // candidate.
    return false;
}


// Tabulate votes for non-eliminated candidates.
void tabulate(void)
{
    // Initiate variable to track if voter's top valid preference was
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
                // Skip eliminated candidates.
                if (candidates[k].eliminated)
                {
                    continue
                }

                // If candidate is not eliminated and is a match with
                // voter preference, then increment candidate's vote
                // count. Break after first non-eliminated preference
                // per voter.
                if (preferences[i][j] == k)
                {
                    candidates[k].votes++;
                    vote_counted = true;
                    break;
                }
            }

            // Move onto next voter if top preference was successfully
            // counted, otherwise check next preference.
            if (vote_counted == true)
            {
                break;
            }
        }
    }

    return;
}


// Print the winner of the election, if there is one
bool print_winner(void)
{
    // Store half the voter count to compare for >50% majority rule.
    float half_voter_count = (float) voter_count / 2

    // Initiate count variable for the highest number of votes, starting
    // at one lower than the lowest possible number.
    int most_votes = -1;

    // Find the highest number of votes from non-eliminated candidates.
    for (int i = 0; i < candidate_count; i++)
    {

        // If any noneliminated candidate has >50% of the votes, print
        // name and return true.
        if (!candidates[i].eliminated &&
            candidates[i].votes > half_voter_count)
        {
            printf("%s\n", candidates[winner_index].name);
            return true;
        }

    // Return false if no majority winner could be printed.
    return false;
}


// Return the minimum number of votes any remaining candidate has.
int find_min(void)
{
    // Initiate count variable for the lowest number of votes, starting
    // at 1 higher than the highest possible number.
    int lose_votes = voter_count + 1;

    // Find the lowest number of votes from a non-eliminated candidate
    // and return number.
    for (int i = 0; i < candidate_count; i++)
    {
        if (!candidates[i].eliminated && candidates[i].votes < lose_votes)
        {
            lose_votes = candidates[i].votes;
        }
    }

    // Return the lowest number of votes found.
    return lose_votes;
}


// Return true if the election is tied between all candidates, false otherwise.
bool is_tie(int min)
{
    // Iterate through all non-eliminated candidates to check if any
    // vote count is greater than the minimum. If so, return false to
    // indicate that the election is not a tie.
    for (int i = 0; i < candidate_count; i++)
    {
        if (!candidates[i].eliminated && candidates[i].votes > min)
        {
            return false;
        }
    }

    // Return true if election is a tie.
    return true;
}


// Eliminate the candidate (or candidates) in last place.
void eliminate(int min)
{
    // Update candidate eliminated status to true if their vote count
    // matches the current lowest number of votes.
    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes == min)
        {
            candidates[i].eliminated = true;
        }
    }

    return;
}
