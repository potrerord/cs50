// Implements a dictionary's functionality.

#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>

#include "dictionary.h"


// Constant: Number of letters.
const unsigned int LETTERS = 26;

// Represents a node in a trie.
typedef struct Node
{
    struct Node *children[LETTERS];
    bool islast;
}
node;

// Global variable for dictionary word count.
unsigned int word_count = 0;

/*
// Hash table
node *table[N];
*/


// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // Use hash(word) to get a hash value

    // Search the hash table at the location specified by the word's
    // hash value.
        // Return true if the word is found



    // Return false if the word is not found.



    return false;
}


// Hashes word to a number
unsigned int hash(const char *word)
{
    // Hash the word to obtain its hash value (case-insensitively - foo
    // and FOO should have the same value. use strcasecmp.)

    /* The hash function given to you returns an int between 0 and 25,
    inclusive, based on the first character of word. However, there are
    many ways to implement a hash function beyond using the first
    character (or characters) of a word. Consider a hash function that
    uses a sum of ASCII values or the length of a word. A good hash
    function reduces “collisions” and has a (mostly!) even distribution
    across hash table “buckets”.
    */






    // return a positive unsigned int for the hash value



    return toupper(word[0]) - 'A';
}


void insert_to_trie(node *trie, char *word)
{
    // Base case: At end of word, mark node as a last letter in a word.
    if (word == '\0')
    {
        node->islast = true;

        // Return true for successful word insertion.
        return true;
    }

    // Recursive case: If not the end, insert letter and create next.
    node *temp = malloc(sizeof(node));
    if (temp == NULL)


    letter = tolower(word) - 'a';
    node->children[letter] = malloc(sizeof(node));

    if
    node->islast = false;
    insert_to_trie(node, word + 1;)


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

    // Allocate and initialize a pointer for a trie root.
    node *root = malloc(sizeof(node));
    for (int i = 0; i < N; i++)
    {
        root->letters[i] = NULL;
    }
    root->islast = false;

    // Did you free this?

    // Variable for holding the converted ASCII -> letter index value.
    int letter;

    // Read each word in the file.
    char c;
    while (fread(&c, sizeof(char), 1, source))
    {
        // Convert ASCII letter character to lowercase 0-25 index.
        letter = tolower(c) - 'a';

        // If trie has NULL child for that letter,
        if (root->children[letter] == NULL)
        {
            // Create space for a new trie node.
            node *temp = malloc(sizeof(node));
            if (temp == NULL)
            {
                return 1;
            }

            root->children[letter] = temp;

        }

        // Create space for a new trie node.
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return 1;
        }


        n->number = x;
        n->next = NULL;



        // Count words for size() function.
        word_count++;
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


// Return number of words in dictionary if loaded, else 0.
unsigned int size(void)
{
    return word_count;
}


// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // Use valgrind with test input for the program like:
    // valgrind ./speller texts/cat.txt


    // Use free() for any allocated memory in load()



    // Use a temp "next" variable to store each node's next value like
    // in lecture.











    return false;
}
