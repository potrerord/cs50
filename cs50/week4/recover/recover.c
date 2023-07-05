// Recovers JPEG data from command-line argument memory card file.

#include <stdio.h>
#include <stdlib.h>


// Constant: Number of bytes per block in FAT file system.
const int BLOCK_SIZE = 512;

// Define data type BLOCK as 512 unsigned integers.
typedef uint8_t BLOCK[BLOCK_SIZE];
typedef uint8_t BYTE;

// Constant: Number of bytes in JPEG signature.
const int SIG_SIZE = 3;

// Constant: first 3 bytes of hex JPEG signature.
const int SIG = {0xff, 0xd8, 0xff};


// Function prototypes.
bool isjpeg(BLOCK subject);



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
    BLOCK buffer;

    // Iteratively read 1 block into buffer until end of file.
    while (fread(buffer, 1, BLOCK_SIZE, card) == BLOCK_SIZE)
    {

        // Skip if the buffer does not contain a JPEG.
        if (!isjpeg(buffer))
        {
            continue;
        }


        // If you use malloc() you need to use free()


        // Scan the 1-3 bytes for 0xff 0xd8 0xff, or 11111111 11011000 11111111 in binary
        // Also scan the 4th byte to see if it starts with 0xe, or 1110 in binary



        // when you find a jpeg signature on the memory card
            // open a new file and write to it from the memory card
                // The files you generate should each be named ###.jpg,
                // where ### is a three-digit decimal number, starting
                // with 000 for the first image and counting up.
                // Use a loop for this
                // printf("%03d" or i? d for decimal)

        // Keep in mind your program should number the files it outputs
        // by naming each ###.jpg, where ### is three-digit decimal
        // number from 000 on up. Befriend sprintf and note that sprintf
        //  stores a formatted string at a location in memory. Given the
        //  prescribed ###.jpg format for a JPEG’s filename, how many
        // bytes should you allocate for that string? (Don’t forget the
        // NUL character!)




        // fclose the file when you encounter another signature


        // Finish when there's no data left to read


        // Free the data you were using


        // Return 0 if successful


    }

}

bool isjpeg(BLOCK subject)
{
    // Check if the first three bytes match the JPEG signature.
    for (int i = 0; i < 3; i++)
        {
            if (subject[i] != SIG[i])
            {
                return false;
            }
        }

    // Check if the first half of the fourth byte is 0xe.
    

    return true;
}