// Want to create a program called recursion.c that calculates factorial

#include <cs50.h>
#include <stdio.>

// Prototypes
int factorial(int n);


// Take user input for n, then print n!.
int main(void)
{
    int n = get_int("Enter a number: ");
    printf("the factorial of %i is %i.\n", n, factorial(n))
}


// Recursively calculate the factorial until n == 0.
int factorial(int n)
{
    // Base case: 0! == 1.
    if (n == 0)
    {
        return 1;
    }
    // Recursive case: any int above 0.
    return n * factorial(n - 1);
}