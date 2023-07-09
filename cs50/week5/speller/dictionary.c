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

    // Read each word in the file.
    char c;
    while (fread(&c, sizeof(char), 1, source))
    {
        
    }



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















    return false;
}
