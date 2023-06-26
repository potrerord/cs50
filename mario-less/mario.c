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
    return h
}

// Prints half-pyramid with height input
void print_hpyramid(int height)
{
    // Print input number of rows
    while (i = 0, i < height, i++)
    {
        // In each row, print decreasing spaces starting with height - 1
        while (j = 0, j < height - 1 - i, j++)
        {
            print(" ");
        }

        // Then print increasing # followed by \n starting with 1
        while (k = 0, 

        // printf()
        // print size-1_ 1"#" "\n"
        // print size-2_ 2# "\n"
        // print size-3_ 3# "\n"
        // print size-size_ size# "\n"
    }


}