// Declares a dictionary's functionality

#ifndef DICTIONARY_H
#define DICTIONARY_H

#include <stdbool.h>

// Maximum length for a word
// (e.g., pneumonoultramicroscopicsilicovolcanoconiosis)
#define LENGTH 45

// Number of letters in the alphabet, plus apostrophe.
#define LETTERS 27

// Represents a node in a trie.
typedef struct Node
{
    struct Node *children[LETTERS];
    bool islast;
}
node;

// Prototypes
bool check(const char *word);
int convert_ascii(char character)
bool free_trie(node *trie);
unsigned int hash(const char *word);
void initialize_node(node *argnode);
void insert_to_trie(node *trie, char *word);
bool load(const char *dictionary);
unsigned int size(void);
bool unload(void);

#endif // DICTIONARY_H
