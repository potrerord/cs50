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

    // Initiate file number variable.
    int file_num = 0;


    // Iteratively read 1 block into buffer until end of file.
    while (fread(buffer_block, 1, BLOCK_SIZE, card) == BLOCK_SIZE)
    {

        // Skip if the buffer does not contain a JPEG.
        if (!isjpeg(buffer_block))
        {
            continue;
        }

        // Number of chars in "###.jpg" filename string, including \\0'.
        const int FILENAME_SIZE = 8;

        // Create name for new JPEG file.
        char filename[FILENAME_SIZE];
        sprintf(filename, "{%03d}.jpg", file_num);

        // Open new file and write to it from the memory card.
        fopen(filename, "w");

        // Increment file number.
        file_num++;

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