// Encrypts messages using custom cipher with cmd-line key input

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//// Rotates chars according to pos int key
char rotate(char c, int key);

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
        // Check every character of arg until '\0' or until > 26 chars, error if nonalpha or > 26 chars
        int j = 0;

        while (argv[1][j] != '\0')
        {
            if (j > 26 || isalpha(argv[1][j]) == 0)
            {
                printf("substitution: error: argument must be 26 alpha characters\n");
                return 1;
            }
            j++;
        }

        // Error if j makes it out of the above loop without getting to 26
        if (j < 26)
        {
            printf("substitution: error: argument must be 26 alpha characters\n");
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

        char alphabet[26];
        for (int i = 0; i < 26; i++)
        {
            alphabet[i] = i + 65;
        }

        // Store argument as integer key
        int key = atoi(argv[1]);

        // Prompt user for plaintext string
        string plaintext = get_string("plaintext:  ");

        // Rotate and print every character in plaintext input according to cmd-line key
        printf("ciphertext: ");
        for (int i = 0, n = strlen(plaintext); i < n; i++)
        {
            printf("%c", rotate(plaintext[i], key));
        }
        printf("\n");
        return 0;
    }
}

// Rotates chars according to pos int key
char rotate(char c, int key)
{
    // Prints nonalpha symbols as-is
    if (isalpha(c) == 0)
    {
        return c;
    }

    else
    {
        // Converts input key to alpha key 0-26 (protects upper limit of int)
        int trueKey = key % 26;

        // Uppercase ascii conversion
        if (isupper(c) != 0)
        {
            return (c + trueKey + 13) % 26 + 65;
        }

        // Lowercase ascii conversion
        else
        {
            return (c + trueKey + 7) % 26 + 97;
        }
    }
}