#include <stdio.h>
#include <stdlib.h>


// Define struct for FAT blocks?
// Each FAT block is 512 bytes



int main(int argc, char *argv[])
{
    // Accept command-line argument.
    

        // argv[1] is the name of a forensic image (memory card) from which to recover JPEGs
        // If not executed with exactly one command line argument, remind user of correct usage and return 1


    // Open the memory card
        // If the forensic image cannot be opened for reading, program should inform user and return 1


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