#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

// Prototypes
char *concatenate(char *s1, char *s2);

int main(void)
{
    // get two strings from the user
    char *s1 = get_string("s1: ");
    char *s2 = get_string("s2: ");

    // create a third string that combines both
    char *s3 = concatenate(s1, s2);

    // print the final string
    printf("%s\n", s3);

    // free up the memory allocated to this
    free(s3);
}

char *concatenate(char *s1, char *s2)
{
    // Discover the length of each of the strings.
    int length1 = strlen(s1);
    int length2 = strlen(s2);
    int total_length = length1 + length2;

    // Allocate the memory for this new string (malloc).
    char *result = malloc((total_length + 1) * sizeof(char));
    if (result == NULL)
    {
        return result;
    }

    // Copy the first string into the combo string.
    for (int i = 0; i < length1; i++)
    {
        result[i] = s1[i];
    }

    // Copy the second string into the combo string.
    for (int i = 0; i < length2; i++)
    {
        result[length1 + i] = s2[i];
    }

    // Add the termination character at the end (\0).
    result[total_length] = '\0';

    // Return the string.
    return result;
}
