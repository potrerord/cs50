#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // Iterate over all pixels in row i and column j.
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int red = image[i][j].rgbtRed;
            int green = image[i][j].rgbtGreen;
            int blue = image[i][j].rgbtBlue;

            // Calculate average of R, G, and B values, rounded to the
            // nearest int.
            int gray_average = (int) round(((red + green + blue) / 3.0));

            image[i][j].rgbtRed = gray_average;
            image[i][j].rgbtGreen = gray_average;
            image[i][j].rgbtBlue = gray_average;
        }
    }






    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{

    // change every pixel to... a shade of brown? like gray but with red?


    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // take every pixel, put into a buffer and then make a new file with the buffer where the width values are flipped?



    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{



    return;
}
