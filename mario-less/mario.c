// Prompts user for an int height and creates a Mario-style half-pyramid with # characters

#include <stdio.h>
#include <cs50.h>

// Continually prompts user for int height until positive
int get_height(void);

// Prints half-pyramid with size input
void print_hpyramid(int size);


int main(void)
{
    // Get height of half-pyramid
    int h = get_height();

    // Print half-pyramid
    print_hpyramid(h);
}










// Continually prompts user for int height until positive
int get_height(void)
{
    int h;
    do
    {
        h = get_int("Height: ");
    }
    while (h < 1);
    return h;
}

// Prints half-pyramid with height input
void print_hpyramid(int height)
{
    // Print input number of rows
    for (int i = 0; i < height; i++)
    {
        // In each row, print decreasing spaces starting with height - 1
        for (int j = 0; j < height - 1 - i; j++)
        {
            printf(" ");
        }

        // Then print increasing # starting with 1
        for (int k = 0; k < i + 1; k++)
        {
            printf("#");
        }

        // Print new line after each row
        printf("\n");
    }
}