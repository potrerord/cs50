// Encrypts messages using custom cipher with cmd-line key input

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//// Rotates chars according to pos int key
// char rotate(char c, int key);

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
        // Error if argument is not proper key (26 chars, all alpha, all 26 letters exactly once)

        for (int i = 0; 1 == 1; i++)
        {
            if (isdigit(argv[1][i]) == 0)
            {
                printf("caesar: error: argument must be alpha\n");
                return 1;
            }
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