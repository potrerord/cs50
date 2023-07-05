// Recovers JPEG data from command-line argument memory card file.

#include <stdio.h>
#include <stdlib.h>


// Number of bytes per block in FAT file system.
const int BLOCK_SIZE = 512;

// Data type definitions.
typedef uint8_t BLOCK[BLOCK_SIZE];

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
    BLOCK buffer_block;

    // Iteratively read 1 block into buffer until end of file.
    while (fread(buffer_block, 1, BLOCK_SIZE, card) == BLOCK_SIZE)
    {

        // Skip if the buffer does not contain a JPEG.
        if (!isjpeg(buffer))
        {
            continue;
        }

        // Initiate file number variable.
        int file_num = 0;

        // Number of characters in a "###.jpg" filename string.
        const int FILENAME_SIZE = 8;

        // Name file.
        while (true)
        {
            // Return error 1 if memory was not successfully allocated.
            if (file == NULL)
            {
                return 1;
            }

            // Create buffer for filename.
            char buffer2[FILENAME_SIZE];

            // Create filename.
            sprintf(buffer2, "###.jpg");

            // Open a new file and write to it from the memory card.
            fopen(filename, "w");
            file_num++;

            // The files you generate should each be named ###.jpg,
            // where ### is a three-digit decimal number, starting
            // with 000 for the first image and counting up.
            // Use a loop for this - printf("%03d" or i? d for decimal)?
            // Keep in mind your program should number the files it outputs
            // by naming each ###.jpg, where ### is three-digit decimal
            // number from 000 on up. Befriend sprintf and note that sprintf
            //  stores a formatted string at a location in memory. Given the
            //  prescribed ###.jpg format for a JPEG’s filename, how many
            // bytes should you allocate for that string? (Don’t forget the
            // NUL character!)



        }


        // fclose the file when you encounter another signature


        // Finish when there's no data left to read


        // Free the data you were using
        // If you use malloc() you need to use free()




    }

    // Return 0 when successful.
    return 0;
}

// Determine if beginning of BLOCK matches JPEG signature.
bool isjpeg(BLOCK subject)
{
    // Number of bytes in JPEG signature.
    const int SIG_SIZE = 4;

    // Bytes 0-2 of hex JPEG signature.
    const int SIG = {0xff, 0xd8, 0xff};

    // Byte 3 of hex JPEG signature (relevant first digit).
    const int SIG_3 = 0xe;

    // Base used in hex integers.
    const int HEX_BASE = 16;

    // Compare against all but the final byte in JPEG signature.
    for (int i = 0; i < SIG_SIZE - 2; i++)
        {
            if (subject[i] != SIG[i])
            {
                return false;
            }
        }

    // Compare against final byte in JPEG signature.
    if (subject[SIG_SIZE - 1] / HEX_BASE) % HEX_BASE != SIG_3
    {
        return false;
    }

    // Return true if signature match.
    return true;
}