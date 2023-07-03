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
bool valid_target(int);
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


// Update preferences given one voter's ranks. Assume that every voter
// will rank each of the candidates.
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
        // challenging candidate in preference[rank[i]][j], aka
        // challenger.
        for (int j = 0; j < candidate_count; j++)
        {
            challenger = preferences[rank_candidate][j];

            // Skip match-ups between self.
            if (challenger == rank_candidate)
            {
                continue;
            }

            // Skip match-ups between a higher-ranked candidate. If
            // challenger matches a rank that is less than the current
            // rank, exit k loop and set already_matched to true to
            // indicate to j loop that this match-up is skipped.
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

            else (preferences[i][j] < preferences[j][i])
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
    // The number of candidates in a given election will never be large
    // enough to require the speed/memory allocation of merge sort - the
    // number of pairs will be even less. It is also not particularly
    // likely that the pairs[] data will arrive sorted in any particular
    // way other than arbitrary candidate numbering order, so selection
    // sort is a good algorithm choice over bubble sort.

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
            if pairs[j].winner > pairs[largest_index].winner
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

    // Check every potential candidate relationship under locked[target]
    // and validate that target.
    for (int i = 0; i < candidate_count; i++)
    {
        
        // If the target has already locked the i'th candidate,
        if locked[target][i]
        {
            if !valid_target(int original, int candidates[i])
            {
                return false;
            }
        }
    }



    // Return true if target is valid.




    // If self is found in target's targets, return false to indicate
    // invalid target.
}


// Lock pairs into the candidate graph in order, without creating
// cycles.
void lock_pairs(void)
{
    // The function should create the locked graph, adding all edges in
    // decreasing order of victory strength so long as the edge would
    // not create a cycle.

    // Iterate over every element in pairs[], in order.


    // Use pairs[i].winner to find row, use pairs[i].loser to find
    // column.


    // Assign true to locked[pairs[i].winner][pairs[i].loser] as long as
    // it wouldn't create a cycle


    // How to check cycle: look at who the loser has already beaten
    // (recursively) and if it's you, cancel the whole operation you're
    // out.


    // To see if x is a valid target, scan x's column to see if they
    // already have any trues. If they do, stop there and see if x is a
    // valid target. Base case is that x has no trues in their column.


    // Call function to scan pairs[i - 1] or whatever



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
