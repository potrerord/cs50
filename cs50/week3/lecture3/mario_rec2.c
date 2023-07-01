// Recursively prints a mario pyramidddddd feels good as hell.

#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

// Prototypes:
void draw(int blocks, int spaces);


// Call the recursive draw function with cmd-line argument.
int main(int argc, string argv[])
{
    int height = atoi(argv[1]);
    draw(height, 0);
}


// Recursively print n rows with base case of n - 1 spaces and one
// block. Default "spaces" value should be 0.
void draw(int blocks, int spaces)
{
    // Base case: Print n - 1 spaces followed by one block.
    if (blocks <= 1)
    {
        for (int i = 0; i < spaces; i++)
        {
            printf(" ");
        }
        printf("#\n");
        return;
    }

    draw(blocks - 1, spaces + 1);

    // Recursive case: Print previous row with one more block and one
    // fewer space.
    for (int i = 0; i < spaces; i++)
    {
        printf(" ");
    }
    for (int i = 0; i < blocks; i++)
    {
        printf("#");
    }
    printf("\n");
    return;
}
