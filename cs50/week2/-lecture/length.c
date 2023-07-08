// Prints int length of name input

#include <cs50.h>
#include <stdio.h>

// Returns int length of string input
int get_length(string input);

int main(void)
{
    string name = get_string("What's your name? ");
    printf("%i\n", get_length(name));
}

// Returns int length of string input
int get_length(string input)
{
    int n = 0;
    while (input[n] != '\0')
    {
        n++;
    }
    return n;
}