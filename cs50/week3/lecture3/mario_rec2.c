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
int draw(int blocks, int spaces)
{
    // Base case: Print 0 spaces.
    if (n <= 0)
    {
        for (int i = spaces; i < blocks; i++)
        {
            
        }
        printf("\n");
        return;
    }

    draw(n - 1, i + 1);

    // Recursive case: Print n - 1 spaces.
    for (int i = 0; i < n - 1; i++)
    {
        printf("-");
    }
    printf("\n");
}
