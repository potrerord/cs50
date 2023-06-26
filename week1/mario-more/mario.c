#include <cs50.h>
#include <stdio.h>

// Continually prompts user for int height until positive
int get_height(void);

// Prints pyramid with height input
void print_pyramid(int height);

int main(void)
{
    // Get height of pyramid
    int h = get_height();

    // Print pyramid
    print_pyramid(h);
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

// Prints pyramid with height input
void print_pyramid(int height)
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

        // Then print 2 spaces
        printf("  ");

        // Then print the same amount of # as before
        for (int k = 0; k < i + 1; k++)
        {
            printf("#");
        }

        // Print new line after each row
        printf("\n");
    }
}