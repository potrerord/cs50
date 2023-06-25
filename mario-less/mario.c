// Prompts user for an int height and creates a Mario-style half-pyramid with # characters

#include <stdio.h>
#include <cs50.h>

// Continually prompts user for positive int height
int get_height(void);


int main(void)
{
    // Get height of half-pyramid
    int h = get_height();

    // Make half-pyramid

    
    // make_pyramid(height)
}










// Continually prompts user for positive int height
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