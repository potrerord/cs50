// Recovers JPEG data from command-line argument memory card file.

#include <stdbool.h>
#include <stdint.h>
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

    // Create buffer for a block of data.
    BLOCK buffer_block;

    // Variables to make "###.jpg" filenames.
    char filename[8];
    int file_num = 0;

    // Iteratively read 1 block into buffer until end of file.
    while (fread(buffer_block, 1, BLOCK_SIZE, card) == BLOCK_SIZE)
    {
        // If file is the start of a new JPEG, close/create new file.
        if (isjpeg(buffer_block))
        {
            fclose(file);

            // Create name for new JPEG file.
            sprintf(filename, "%03d.jpg", file_num);

            // Write new JPEG file from the memory card.
            FILE *file = fopen(filename, "w");
            if (file != NULL)
            {
                fwrite(buffer_block, 1, BLOCK_SIZE, file);
                file_num++;
                if (file_num > 999)
                {
                    printf("error: filename exceeds \"999.jpg\"\n");
                    return 2;
                }
            }
            else
            {
                printf("error: could not create jpeg file.\n");
                return 3;
            }
            ;
        }

        // Write new JPEG file from the memory card.
        FILE *file = fopen(filename, "w");
        if (file != NULL)
        {
            fwrite(buffer_block, 1, BLOCK_SIZE, file);
            fclose(file);
            file_num++;
            if (file_num > 999)
            {
                printf("error: filename exceeds \"999.jpg\"\n");
                return 2;
            }
        }
        else
        {
            printf("error: could not create jpeg file.\n");
            return 3;
        }
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
    const int SIG[SIG_SIZE - 1] = {0xff, 0xd8, 0xff};

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
    if ((subject[SIG_SIZE - 1] / HEX_BASE) % HEX_BASE != SIG_3)
    {
        return false;
    }

    // Return true if signature match.
    return true;
}
