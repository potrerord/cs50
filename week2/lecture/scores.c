// Prints the average of 3 user input test scores

#include <stdio.h>
#include <cs50.h>

const int N = 3

// Returns the average of an array of 3 elements
float average(int array[]);

int main(void)
{
    int scores[N];
    for (int i = 0; i < N; i++)
    {
        scores[i] = get_int("Score %i: ", i + 1);
    }
    printf("Average: %f\n", average(scores));
}

// Returns the average of an array of ints
float average(int array[])
{
    int sum = 0
    for (int j = 0; j < ; j++)
    {
        sum += array[j]
        float average = sum / (float)k
    }
    return average
}
