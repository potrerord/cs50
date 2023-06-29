// Encrypts messages using custom cipher with cmd-line key input

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//// Rotates chars according to pos int key
char substitute(char c, string key);

int main(int argc, string argv[])
{
    // Error if amount of arguments != 1
    if (argc != 2)
    {
        printf("caesar: error: one argument required\n");
        return 1;
    }

    // If single argument
    else
    {
        // Store key in string variable
        string key = argv[1];

        // Check every character of key until '\0' or until > 26 chars, error if nonalpha or > 26 chars
        int j = 0;

        while (key[j] != '\0')
        {
            if (j > 26 || isalpha(key[j]) == 0)
            {
                printf("substitution: error: key must be 26 alpha characters\n");
                return 1;
            }
            j++;
        }

        // Error if j makes it out of the above loop without getting to 26
        if (j < 26)
        {
            printf("substitution: error: key must be 26 alpha characters\n");
            return 1;
        }

        // Getting to here means arg is 26 chars and all alpha

        // convert lowercase to uppercase to compare values


        // compare letters?
        // store each character in a reference array (intialize with
        // char0 is A so it goes in
        // char1 is B so it gets checked with A, all good
        // char2 is C so it gets checked with A B all good
        // char3 is B so it gets checked with A B uh oh now the count variable is 1 so error

        // Initialize reference array to check key against itself for duplicates
        char reference[26];
        for (int i = 0; i < 26; i++)
        {
            reference[i] = 0;
        }

        // Check all 26 alpha chars in key for duplicates
        for (int i = 0; i < 26; i++)
        {
            reference[i] = toupper(key[i]);

            // In each iteration, check to make sure the previous elements in reference[26] did not have the same letter
            for (int k = 0; k < i; k++)
            {
                if (reference[k] == toupper(key[i]))
                {
                    printf("substitution: error: key must have no duplicates\n");
                    return 1;
                }
            }
        }

        // Prompt user for plaintext string
        string plaintext = get_string("plaintext:  ");

        // Encrypt
        printf("ciphertext: ");
        for (int i = 0, n = strlen(plaintext); i < n; i++)
        {
            printf("%c", substitute(plaintext[i], key));
        }
        printf("\n");
        return 0;
    }
}

// Substitutes chars according to key alphabet
char substitute(char c, string key)
{
    // Prints nonalpha symbols as-is
    if (isalpha(c) == 0)
    {
        return c;
    }

    // Not complete, but do something like convert the ascii code to 1-26 regardless of lower/uppercase and then use that 1-26 code to locate the key[i] that it should be instead
    else
    {
         // Uppercase ascii conversion
        if (isupper(c) != 0)
        {
            // Upper means subtract 65 to find out 0-25 code
            c 

            // return (c + trueKey + 13) % 26 + 65;
        }

        // Lowercase ascii conversion
        else
        {
            return c;
        }
    }
}