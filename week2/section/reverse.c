// Reverses a string

#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
    string s = get_string("Enter string: ");
    int length = strlen(s);
    char srev[length];
    int n = 0;

    // Iterates over s and places char in reverse index in array
    for (int i = 0; i < length; i++)
    {
        n = length - i - 1;
        srev[n] = s[i];
    }

    // Prints reverse string with new line at end
    for (int i = 0; i < length ; i++)
    {
        printf("%c", srev[i]);
    }
    printf("\n");
}