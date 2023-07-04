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
            // Store R/G/B values for the pixel.
            int red = image[i][j].rgbtRed;
            int green = image[i][j].rgbtGreen;
            int blue = image[i][j].rgbtBlue;

            // Take average of R/G/B values, rounded to the nearest int.
            int gray_average = (int) round(((red + green + blue) / 3.0));

            // Update pixel values in array.
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

    // Iterate over all pixels in row i and column j.
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Store R/G/B values for the pixel.
            int red = image[i][j].rgbtRed;
            int green = image[i][j].rgbtGreen;
            int blue = image[i][j].rgbtBlue;

            // Store sepia conversion factors for red, green and blue.
            // Each factor is listed in R, G, B order.
            float red_sepia_factors[3] = {0.393, 0.769, 0.189};
            float green_sepia_factors[3] = {0.349, 0.686, 0.168};
            float blue_sepia_factors[3] = {0.272, 0.534, 0.131};

            // Update pixel values in array.
            image[i][j].rgbtRed = ;
            image[i][j].rgbtGreen = ;
            image[i][j].rgbtBlue = ;
        }
    }

    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // Iterate over all pixels in row i and column j.
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Declare variables to store R/G/B values for the pixel.
            int red = image[i][j].rgbtRed;
            int green = image[i][j].rgbtGreen;
            int blue = image[i][j].rgbtBlue;

            //


            // Update pixel values in array.
            image[i][j].rgbtRed = ;
            image[i][j].rgbtGreen = ;
            image[i][j].rgbtBlue = ;
        }
    }

    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{



    return;
}
