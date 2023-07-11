"""
Prompts user for an int height and creates a Mario-style half-pyramid
with # characters.
"""


def main():
    """Take user input and print pyramid."""

    # Get height of half-pyramid
    height = get_height();

    # Print half-pyramid
    print_hpyramid(height);


def get_height() -> int:
"""Return user-input positive integer pyramid height."""

    while True:
        h = get_int("Height: ")

        if not(h > 0):
            break

    return h

// Prints half-pyramid with height input
void print_hpyramid(int height)
{
    // Print input number of rows
    for (int i = 0; i < height; i++)
    {
        // In each row, print decreasing spaces starting with height - 1
        for (int j = 0; j < height - 1 - i; j++)
        {
            printf(" ");
        }

        // Then print increasing # starting with 1
        for (int k = 0; k < i + 1; k++)
        {
            printf("#");
        }

        // Print new line after each row
        printf("\n");


if __name__ == "__main__":
    main()
