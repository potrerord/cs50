// Prints the average of 3 user input test scores

#include <stdio.h>
#include <cs50.h>

const int N = 3;

// Returns the average of an array of 3 elements
float average(int array[], int length);

int main(void)
{
    int scores[N];
    for (int i = 0; i < N; i++)
    {
        scores[i] = get_int("Score %i: ", i + 1);
    }
    printf("Average: %f\n", average(scores, N));
}

// Returns the average of an array of ints
float average(int array[], int length)
{
    int sum = 0;
    for (int i = 0; i < length; i++)
    {
        sum += array[i];
    }
    return sum / (float) length;
}
