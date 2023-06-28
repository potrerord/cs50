// Encrypts messages using Caesar cipher with cmd-line key input

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

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
        // Error if argument is not nonnegative int
        for (int i = 0; 1 == 1; i++)
        {
            if (argv[1][i] == '\0')
            {
                break;
            }
            else if (isdigit(argv[1][i]) == 0)
            {
                printf("Usage: ./caesar key\n");
                return 1;
                break;
            }
        }

        // If argument is nonnegative int, continue to main function

        // Even if k is greater than 26, alphabetical characters in your program’s input
        // should remain alphabetical characters in your program’s output.
        // For instance, if k is 27, A should not become \ even though \ is 27 positions away from
        // A in ASCII,per asciitable.com; A should become B, since B is 27 positions away from A,
        // provided you wrap around from Z to A.

        // Prompt user for plaintext string
        string plaintext = get_string("plaintext:  ");

        // Rotate alphabet according to key, ignoring nonalpha chars


        // Print encrypted ciphertext
        printf("ciphertext: ");
        for (int i = 0, n = strlen(plaintext); i < n; i++)
        {
            printf('%c', ciphertext[i] + (int) (argv) % 26);
        }
        printf("\n");

        // Your program must preserve case: capitalized letters, though rotated, must remain
        // capitalized letters; lowercase letters, though rotated, must remain lowercase letters.

        // After outputting ciphertext, you should print a newline.
        // Your program should then exit by returning 0 from main.
    }
}