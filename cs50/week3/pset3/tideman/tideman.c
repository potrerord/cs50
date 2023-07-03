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
bool valid_target(int original, int target);
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
        if (strcasecmp(name, candidates[i]) == 0)
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


// Update preferences given one voter's ranks. Assume that every voter
// will rank each of the candidates.
void record_preferences(int ranks[])
{

    // Initiate variables to keep track of array cells by name.

    // Candidate in i loop at the currently-indexed rank:
    int rank_candidate;

    // Candidate in j loop that rank_candidate is being compared to:
    int challenger;

    // Iterate through rank list and assign a vote for every candidate
    // against every candidate below them in the ranking. Initiating j
    // at i + 1 will avoid self-match-ups and previous match-ups
    // automatically.
    for (int i = 0; i < candidate_count - 1; i++)
    {
        rank_candidate = ranks[i];

        // Scan through candidate list to compare rank_candidate against
        // challenging candidate.
        for (int j = i + 1; j < candidate_count; j++)
        {
            challenger = ranks[j];
            preferences[rank_candidate][challenger]++;
        }
    }

    return;
}


// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    // Update global pair count using n_C_r (combinatorics), aka
    // "candidate_count choose 2", as calculated in the formula below.
    pair_count = candidate_count * (candidate_count - 1) / 2;

    // Every vote count in preferences array is fully updated at this
    // point, so scan all pairs and add to pairs[] array. Initiate
    // pairs_index counter variable to track index of pairs[] array.
    int pairs_index = 0;

    // Iterate through every match-up in preferences array with i
    // and j. Previous pairs and self-pairs are skipped naturally
    // with j initiating at i + 1, and total will naturally not
    // exceed pair_count.
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = i + 1; j < candidate_count; j++)
        {
            // Skip ties, no need to increment pairs_index.
            if (preferences[i][j] == preferences[j][i])
            {
                continue;
            }

            // Add winners and losers to pairs[] array.
            if (preferences[i][j] > preferences[j][i])
            {
                pairs[pairs_index].winner = i;
                pairs[pairs_index].loser = j;
            }

            else
            {
                pairs[pairs_index].winner = j;
                pairs[pairs_index].loser = i;
            }

            // Increment pairs_index inside i/j loop to maintain
            // progress while scanning preferences[] array.
            pairs_index++;
        }
    }

    return;
}


// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{
    /* Note: The number of candidates in a given election will never be
    large enough to require the speed/memory allocation of merge sort -
    the number of pairs will be even less. It is also not likely that
    the pairs[] data will arrive sorted in any particular way other than
    arbitrary candidate numbering order, so selection sort is a good
    algorithm choice. */

    // Create tracker variable for largest winner vote count per pair.
    int largest_index;

    // Create temporary storage variable of type pair to switch data
    // points.
    pair temp_storage;

    // Begin each scan at pairs[i].
    for (int i = 0; i < pair_count; i++)
    {
        largest_index = i;

        // Scan through every element after pairs[i] to identify index
        // of largest value after pairs[i], and update largest_index
        // accordingly.
        for (int j = i + 1; j < pair_count; j++)
        {
            if (preferences[pairs[j].winner][pairs[largest_index].winner] >
                preferences[pairs[largest_index].winner][pairs[j].winner])
            {
                largest_index = j;
            }
        }

        // Switch pairs[i] with value at largest_index (even if equal,
        // for simplicity).
        temp_storage = pairs[i];
        pairs[i] = pairs[largest_index];
        pairs[largest_index] = temp_storage;
    }

    return;
}


// Validate target of "arrow" in Tideman voting method graph by
// recursively calling self to scan target's targets.
bool valid_target(int original,int target)
{
    // Base case: If target matches original caller, return false.
    if (target == original)
    {
        return false;
    }

    // Check all candidates to see if target has locked them. If the
    // target has locked a candidate, check to see if that candidate is
    // a valid target.
    for (int i = 0; i < candidate_count; i++)
    {
        if (locked[target][i])
        {
            if (!valid_target(original, i))
            {
                return false;
            }
        }
    }

    // If function has checked every potential target and not found the
    // original, then return true.
    return true;
}


// Lock pairs into the candidate graph in order, without creating
// cycles.
void lock_pairs(void)
{
    // Iterate over every element in pairs[].
    for (int i = 0; i < pair_count; i++)
    {

        // If the winner of this pair is allowed to lock the loser of
        // this pair, mark the relationship as locked.
        if (valid_target(pairs[i].winner, pairs[i].loser))
        {
            locked[pairs[i].winner][pairs[i].loser] = true;
        }
    }

    return;
}


// Print the winner of the election
void print_winner(void)
{
    // Create unlocked_count variable to trigger printf statement at the
    // end of the function.
    int unlocked_count;

    // Iterate over every potential winner.
    for (int i = 0; i < candidate_count; i++)
    {
        // Reset unlocked_count for new candidate.
        unlocked_count = 0;

        // Use j to scan threats to this candidate for "true" locks. If
        // candidate has not been locked by any other candidates,
        // unlocked_count will make it to candidate_count and trigger
        // printf statement announcing winner.
        for (int j = 0; j < candidate_count; j++)
        {
            if (locked[j][i])
            {
                break;
            }

            unlocked_count++;
        }

        if (unlocked_count == candidate_count)
        {
            printf("%s\n", candidates[i]);
        }
    }

    return;
}
