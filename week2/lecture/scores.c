// Prints the average of 3 user input test scores

#include <stdio.h>
#include <cs50.h>

// Returns the average of an array of 3 elements
float average(int array[]);

int main(void)
{
    int scores[3];
    for (int i = 0; i < 3; i++)
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
