// Prompts user for an int height and creates a Mario-style half-pyramid with # characters

#include <stdio.h>
#include <cs50.h>

// Continually prompts user for int height until positive
int get_height(void);

// Prints the half-pyramid
void print_pyramid(int size);


int main(void)
{
    // Get height of half-pyramid
    int h = get_height();

    // Print half-pyramid of height h
    print()
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

// Prints pyramid of size h
void print_pyramid(int size)
{
    
}