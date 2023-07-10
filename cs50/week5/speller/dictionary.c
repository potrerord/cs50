// Implements a dictionary's functionality.


#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "dictionary.h"


// Global variable for dictionary word count.
unsigned int word_count = 0;

// Global root for trie.
node *root;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // Initialize looped pointer variable at root pointer.
    node *ptr = root;

    // Prepare to convert letter indices.
    int letter;

    // For each character in word:
    for (int i = 0, wordlen = strlen(word); i < wordlen; i++)
    {
        // Convert letter to index.
        letter = tolower(word[i]) - 'a';

        // If there is no child for that letter, return false
        if (ptr->children[letter] == NULL)
        {
            return false;
        }

        // If there is, move ptr to child.
        ptr = ptr->children[letter];

        // If ptr is at the last letter of the word,
        if (i == wordlen - 1)
        {
            // Return true if the current node is a last letter.
            if (ptr->islast == true)
            {
                return true;
            }
        }
    }

    // If word is not in trie, return false.
    return false;
}


/*
// Hashes word to a number
unsigned int hash(const char *word)
{
    return toupper(word[0]) - 'A';
}
*/


void initialize_node(node *argnode)
{
    for (int i = 0; i < LETTERS; i++)
    {
        argnode->children[i] = NULL;
    }

    argnode->islast = false;
}


void insert_to_trie(node *trie, char *word)
{
    // Convert char to letter index.
    int letter = tolower(*word) - 'a';

    // If a node doesn't already exist at that letter,
    if (trie->children[letter] == NULL)
    {
        // Create temp node and exit program if failed.
        node *ptr = malloc(sizeof(node));
        if (ptr == NULL)
        {
            printf("error: memory allocation failed\n");
            exit(1);
        }

        // Initialize temp node.
        initialize_node(ptr);

        // Point current trie's child for this letter at new node.
        trie->children[letter] = ptr;
    }

    // Base case: If next character is '\0', mark current as last.
    if (word[1] == '\0')
    {
        trie->children[letter]->islast = true;
        return;
    }

    // Recursive case: If more letters to insert, insert next node.
    insert_to_trie(trie->children[letter], word + 1);

    return;
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


// Return number of words in dictionary if loaded, else 0.
unsigned int size(void)
{
    return word_count;
}


// Recursively free trie.
bool free_trie(node *trie)
{
    // Base case:


    // Recursive case: For each child in node,
    for (int i = 0; i < LETTERS; i++)
    {
        // If child is not NULL,
        if (trie->children[i] != NULL)
        {
            // Free child.
            free_trie(trie->children[i]);
        }
    }

    // Base case: If all children are NULL, free current node.
    free(trie);
    return true;
}


// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    bool freed = false;
    freed = free_trie(root);
    return freed;
}
