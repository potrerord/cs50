// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "dictionary.h"


// Global variable for dictionary word count.
unsigned int word_count = 0;

// Represents a node in a hash table.
typedef struct Node
{
    char word[LENGTH + 1];
    struct Node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];


// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    return false;
}


// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return toupper(word[0]) - 'A';
}


// Load dictionary into memory, return true if successful/false if not.
bool load(const char *dictionary)
{
    // Open dictionary
    FILE *source = fopen(dictionary, "r");

    // Return false if file was not opened.
    if (source == NULL)
    {
        return false;
    }

    // Create temp node for root and exit program if failed.
    node *temp = malloc(sizeof(node));
    if (temp == NULL)
    {
        printf("error: memory allocation failed\n");
        exit(1);
    }

    // Initialize temp node.
    initialize_node(temp);

    // Assign allocated memory for node to root pointer.
    root = temp;

    // Prepare to assemble words.
    int index = 0;
    char word[LENGTH + 1];
    char c;

    // Assemble words from dictionary.
    while (fread(&c, sizeof(char), 1, source))
    {
        // Assume all lowercase/apostrophes and separated by \n.
        if (c != '\n')
        {
            // Append character to word.
            word[index] = c;
            index++;
        }

        // New line means the word is over.
        else if (index > 0)
        {
            // Terminate current word.
            word[index] = '\0';

            // Insert word to trie.
            insert_to_trie(root, word);

            // Increment global word count.
            word_count++;

            // Prepare for next word.
            index = 0;
        }
    }

    // Close file and return true for successful load.
    fclose(source);
    return true;
}


// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return 0;
}


// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    return false;
}
