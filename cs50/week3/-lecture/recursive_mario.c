// Recursively prints a mario pyramid (upside down though :/).

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
int print_pyr(int n)
{
    // Base case: Print one block.
    if (n == 1)
    {
        printf("#\n");
        return 1;
    }

    // Recursive case: Print n blocks with a new line.
    for (int i = 0; i < n; i++)
    {
        printf("#");
    }
    printf("\n");
    return print_pyr(n - 1);
}
