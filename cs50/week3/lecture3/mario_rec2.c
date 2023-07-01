// Recursively prints a mario pyramid.

#include <cs50.h>
#include <stdio.h>

// Prototypes:
int print_pyr(int n);


// Call the recursive print_pyr function.
int main(void)
{
    int height = get_int("Enter height: ");
    print_pyr(height);
}


// Recursively print n rows with base case n = #.
int draw_row(int n)
{

    // Base case: print n blocks.
    if (int frame == n)
    {
        // Print n blocks with no spaces for the bottom row.
        for (int i = 0; i < n; i++)
        {
            printf("#");
        }
        printf("\n");
    }

    // Recursive case: Print previous row with 1 less block and 1 more
    // space.
    for (int i = 0; i < n; i++)
    {
        printf("#");
    }
    printf("\n");
    return print_pyr(n - 1);
}
