#include <cs50.h>
#include <stdio.h>


// Prototypes
int triangular(int n);


int main(void)
{
    int user_n = get_int("Enter positive int: ");
    int user_triangular = triangular(user_n);
    printf("%i", triangular(user_n));
}


// Recursively calculate the nth triangular number.
int triangular(int n)
{
    // Base case: the first triangular number is 1.
    if (n == 1)
    {
        return 1;
    }

    // Add n to the previous triangular number.
    n = n + triangular(n);
    return n;
}
