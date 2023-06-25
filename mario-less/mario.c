// Prompts user for an int height and creates a Mario-style half pyramid with # characters

#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // Prompts user for height
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while (height < 0);
    
}


// get_height()
// make_pyramid(height)