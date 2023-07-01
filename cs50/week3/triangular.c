// Recursively calcuates the nth triangular number.

#include <cs50.h>
#include <stdio.h>


// Prototypes
int triangular(int n);


int main(int argc, string argv[])
{
    int user_n = atoi(argv[1]);
    int user_triangular = triangular(user_n);
    printf("%i", user_triangular);
}


// Recursively calculate the nth triangular number.
int triangular(int n)
{
    // Base case: The first triangular number is 1.
    if (n == 1)
    {
        return 1;
    }

    // Recursive case: Add n to the previous triangular number.
    return n + triangular(n);
}
