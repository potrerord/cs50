// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // Hash the word to obtain its hash value (case-insensitively - foo
    // and FOO should have the same value. use strcasecmp.)


    // Search the hash table at the location specified by the word's
    // hash value.
        // Return true if the word is found

    // Return false if the word is not found.










    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{











    return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // Open dictionary
    FILE *source = fopen(dictionary, "r");

    // Return false if unsuccessful.
    if (source == NULL)
    {
        return false;
    }

    // Create a pointer for a linked list.
    node *list = NULL;

    // Create a word count variable?



    // Read each word in the file.
    char c;
    while (fread(&c, sizeof(char), 1, source))
    {
        // Create space for a new hash table node.
        node *n = malloc(sizeof(node));
        n->number = x;
        n->next = NULL;


        // Count each word and save in malloc so it exists after load().

    }

    // TODO: Add new node to head (front) of linked list.
    n->next = list;
    list->next = n;

    // Update the total number of nodes
    totalNodes++;



    // Copy the word into the new node.



    // Hash the word to obtain its hash value.



    // Insert the new node into the hash table (using the index
    // specified by its hash value)



    // Return false if unsuccessful (again, at any other point)



    // Close file and return true for successful load.
    fclose(source);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{













    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // Use valgrind with test input for the program like:
    // valrgind ./speller texts/cat.txt


    // Use free() for any allocated memory in load()



    // Use a temp "next" variable to store each node's next value like
    // in lecture.











    return false;
}
