// Reverses a string

#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
    string s = get_string("Enter string: ");
    int length = strlen(s);
    char array[length];
    int n = 0;

    for (int i = 0; i < length; i++)
    {
        n = length - i - 1;
        array[n] = s[i];
    }
    for (int i = 0; i < length ; i++)
    {
        printf("%c", array[i]);
    }
    printf("\n");
}