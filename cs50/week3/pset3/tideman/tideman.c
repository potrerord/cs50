#include <cs50.h>
#include <stdio.h>
#include <strings.h>

// Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX];

// locked[i][j] means i is locked in over j
bool locked[MAX][MAX];

// Each pair has a winner, loser
typedef struct
{
    int winner;
    int loser;
}
pair;

// Array of candidates
string candidates[MAX];
pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

// Function prototypes
bool vote(int rank, string name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
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
        candidates[i] = argv[i + 1];
    }

    // Clear graph of locked in pairs
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;
        }
    }

    pair_count = 0;
    int voter_count = get_int("Number of voters: ");

    // Query for votes
    for (int i = 0; i < voter_count; i++)
    {
        // ranks[i] is voter's ith preference
        int ranks[candidate_count];

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
        }

        record_preferences(ranks);

        printf("\n");
    }

    add_pairs();
    sort_pairs();
    lock_pairs();
    print_winner();
    return 0;
}

// Update ranks given a new vote.
bool vote(int rank, string name, int ranks[])
{
    // Check for match between vote name (argument) and candidate name
    // from candidates[]. Assume no two candidates have the same name.
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcasecmp(name, candidates[i].name) == 0)
        {

        // If match is found, update the ranks array to indicate that
        // the voter has the ith candidate as their [rank] preference.
        // Return true if successfully recorded.
            ranks[rank] = i;
            return true;
        }
    }

    // Return false to indicate vote that was not successfully recorded.
    return false;
}

// Update preferences given one voter's ranks.
void record_preferences(int ranks[])
{

    // Initiate variables to keep track of array cells by name.

    // Candidate in i loop at the currently-indexed rank:
    int rank_candidate;

    // Candidate in j loop that rank_candidate is being compared to:
    int challenger;

    // Used in k loop to check if challenger has already been a higher-
    // ranked candidate.
    int prev_rank_candidate;

    // Boolean value to indicate match-ups that have already occurred.
    bool already_matched;

    // Iterate through each of the voter's ranks, i (starting from 0) to
    // find their i'th ranked candidate, ranks[i]. Last candidate will
    // have no one-on-one victories, so amount of iterations can be
    // decreased by 1 from candidate_count.
    for (int i = 0; i < candidate_count - 1; i++)
    {
        rank_candidate = ranks[i];

        // Scan through second dimension of preferences[rank[i]] to log
        // all of candidate's incremental one-on-one victories against
        // candidate in preference[rank[i]][j], aka challenger.
        for (int j = 0; j < candidate_count; j++)
        {
            challenger = preferences[rank_candidate][j];

            // Avoid match-ups between self.
            if (challenger == rank_candidate)
            {
                continue;
            }

            // Avoid match-ups between a higher-ranked candidate.
            // If challenger matches a rank that is less than the
            // current rank, exit loop and set already_matched to true
            // to indicate to outer loop that this match-up is skipped.
            already_matched = false;

            for (int k = 0; k < i; k++)
            {
                prev_rank_candidate = rank[k];
                if (challenger == prev_rank_candidate)
                {
                    already_matched = true;
                }
            }

            if (already_matched)
            {
                continue;
            }

            // Increment all other match-ups by 1 for this rank.
            preferences[rank_candidate][challenger]++;
        }
    }


    // You may assume that every voter will rank each of the candidates.



    return;
}

// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    // The function should add all pairs of candidates where one
    // candidate is preferred to the pairs array.



    // A pair of candidates who are tied (one is not preferred over the
    // other) should not be added to the array.



    // The function should update the global variable pair_count to be
    // the number of pairs of candidates. (The pairs should thus all be
    // stored between pairs[0] and pairs[pair_count - 1], inclusive).



    return;
}

// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{
    // The function should sort the pairs array in decreasing order of
    // strength of victory, where strength of victory is defined to be
    // the number of voters who prefer the preferred candidate.



    // If multiple pairs have the same strength of victory, you may
    // assume that the order does not matter.



    return;
}

// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{
    // The function should create the locked graph, adding all edges in
    // decreasing order of victory strength so long as the edge would
    // not create a cycle.



    return;
}

// Print the winner of the election
void print_winner(void)
{
    // The function should print out the name of the candidate who is
    // the source of the graph. You may assume there will not be more
    // than one source.



    return;
}