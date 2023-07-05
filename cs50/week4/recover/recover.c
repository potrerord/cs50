#include <stdio.h>
#include <stdlib.h>


typedef uint8_t BYTE;

typedef struct
{
    BYTE
}


int main(int argc, char *argv[])
{
    // Accept a single command-line argument.
    if (argc != 2)
    {
        printf("Usage: ./ recover FILE\n");
        return 1;
    }

    // Open the memory card.
    FILE *card = fopen(argv[1], "r");
    if (card == NULL)
    {
        printf("error: card could not be opened\n");
        return 1;
    }


    // Create a buffer for a block of data.
    uint8_t buffer[512];


    // If you use malloc() you need to use free()


    // loop for each block of 512 bytes
    // Scan the 1-3 bytes for 0xff 0xd8 0xff, or 11111111 11011000 11111111 in binary
    // Also scan the 4th byte to see if it starts with 0xe, or 1110 in binary



    // when you find a jpeg signature on the memory card
        // open a new file and write to it from the memory card
            // The files you generate should each be named ###.jpg, where ### is a three-digit decimal number, starting with 000 for the first image and counting up.
            // Use a loop for this
            // printf("%03d" or i? d for demical)


    // close the file when you encounter another signature


    // Finish when there's no data left to read


    // Free the data you were using


    // Return 0 if successful


}