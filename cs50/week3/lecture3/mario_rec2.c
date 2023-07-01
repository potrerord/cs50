// Recursively prints a mario pyramid (upside down though :/).

#include <cs50.h>
#include <stdio.h>

// Prototypes:
int draw(int n);


// Call the recursive print_pyr function.
int main(void)
{
    int height = get_int("Enter height: ");
    draw(height);
}


// Recursively print n rows with base case n = space.
// Ideally, figure out a way for default spaces to be 0.
int draw(int blocks, int spaces)
{
    // Base case: Print n - 1 blocks.
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

    // Recursive case: Print n - 1 spaces.
    for (int i = 0; i < n - 1; i++)
    {
        printf("-");
    }
    printf("\n");
}
