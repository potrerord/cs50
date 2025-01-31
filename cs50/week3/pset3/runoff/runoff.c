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


// Record preference if vote is valid.
bool vote(int voter, int rank, string name)
{
    // Check every candidate name for match with vote. Ignores case.
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcasecmp(name, candidates[i].name) == 0)
        {
            // Log candidate number with appropriate voter and rank,
            // then return true to indicate successful vote.
            preferences[voter][rank] = i;
            return true;
        }
    }

    // Return false to indicate invalid vote.
    return false;
}


// Tabulate votes for non-eliminated candidates.
void tabulate(void)
{
    // Create variable to track voter number in i loop.
    int voter_number;

    // Create variable to track current voter preference in j loop.
    int current_preference;

    // Initiate variable to track successful vote count.
    bool vote_counted = false;

    // Iterate through each voter.
    for (int i = 0; i < voter_count; i++)
    {
        voter_number = i;

        // Reset vote_counted status.
        vote_counted = false;

        // Iterate through voter preferences.
        for (int j = 0; j < candidate_count; j++)
        {
            current_preference = preferences[voter_number][j];

            // Iterate through candidate list.
            for (int k = 0; k < candidate_count; k++)
            {
                // Skip eliminated candidates.
                if (candidates[k].eliminated)
                {
                    continue;
                }

                // If candidate matches voter's current preference,
                // increment candidate's vote count.
                if (current_preference == k)
                {
                    candidates[k].votes++;
                    vote_counted = true;

                    // Exit candidate list after first successful match.
                    break;
                }
            }

            // Move onto next voter if top preference was counted.
            if (vote_counted == true)
            {
                break;
            }
        }
    }

    // Return after every vote has been logged.
    return;
}


// Print the winner of the election, if there is one.
bool print_winner(void)
{
    // Store 50% vote_count to check majority win.
    float half_voter_count = (float) voter_count / 2;

    // Initiate count variable for the highest number of votes, starting
    // at 1 lower than the lowest possible number.
    int most_votes = -1;

    // Find the highest number of votes from non-eliminated candidates.
    for (int i = 0; i < candidate_count; i++)
    {
        // Skip eliminated candidates.
        if (candidates[i].eliminated)
        {
            continue;
        }

        // If any noneliminated candidate has majority, print name and
        // return true.
        if (candidates[i].votes > half_voter_count)
        {
            printf("%s\n", candidates[i].name);
            return true;
        }
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

    // Find the lowest number of votes from a noneliminated candidate.
    for (int i = 0; i < candidate_count; i++)
    {

        // Skip eliminated candidates.
        if (candidates[i].eliminated)
        {
            continue;
        }

        if (candidates[i].votes < lose_votes)
        {
            lose_votes = candidates[i].votes;
        }
    }

    // Return lowest number of votes found.
    return lose_votes;
}


// Return true if the election is tied between all candidates, false otherwise.
bool is_tie(int min)
{
    // Check if any noneliminated candidate has a >min vote count.
    for (int i = 0; i < candidate_count; i++)
    {
        // Skip eliminated candidates.
        if (candidates[i].eliminated)
        {
            continue;
        }

        // Return false if any candidate has >min votes and election is
        // not a tie.
        if (candidates[i].votes > min)
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
    // Eliminate candidates if their vote count matches the current min.
    for (int i = 0; i < candidate_count; i++)
    {
        // Skip candidates already eliminated.
        if (candidates[i].eliminated)
        {
            continue;
        }

        // Eliminate candidates.
        if (candidates[i].votes == min)
        {
            candidates[i].eliminated = true;
        }
    }

    // Return once all minimum-vote candidates have been eliminated.
    return;
}
