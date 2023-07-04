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
            int r_orig = image[i][j].rgbtRed;
            int g_orig = image[i][j].rgbtGreen;
            int b_orig = image[i][j].rgbtBlue;

            // Take average of R/G/B values, rounded to the nearest int.
            int gray_avg = (int) round(((r_orig + g_orig + b_orig) / 3.0));

            // Update pixel values in array.
            image[i][j].rgbtRed = gray_avg;
            image[i][j].rgbtGreen = gray_avg;
            image[i][j].rgbtBlue = gray_avg;
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
            int rgb_orig[3] = {image[i][j].rgbtRed,
                               image[i][j].rgbtGreen,
                               image[i][j].rgbtBlue}

            // Store sepia conversion factors for red, green and blue.
            // Each factor is listed in R, G, B order.
            float r_factors[3][3];
            r_factors[0] = {0.393, 0.769, 0.189};
            float g_factors[3] = {0.349, 0.686, 0.168};
            float b_factors[3] = {0.272, 0.534, 0.131};

            // Convert R/G/B values to sepia, rounded to nearest int.
            float rgb_sep[3] = {0.0};

            for (int k = 0; k < 3; k++)
            {
                for (int l = 0; l < 3; l++)
                {
                    rgb_sep[k] += (rgb_orig[l] * r_factors[l]);

                }
            }

            int rgb_sep[0] = (int) round(((r_orig * r_factors[0]) +
                                          (g_orig * r_factors[1]) +
                                          (b_orig * r_factors[2])));

            int rgb_sep[1] = (int) round(((r_orig * g_factors[0]) +
                                          (g_orig * g_factors[1]) +
                                          (b_orig * g_factors[2])));

            int rgb_sep[2] = (int) round(((r_orig * b_factors[0]) +
                                          (g_orig * b_factors[1]) +
                                          (b_orig * b_factors[2])));

            // Cap each converted sepia value at 255.
            int rgb_sep[3] = {r_sep, g_sep, b_sep};
            for (int k = 0; k < 3; k++)
            {
                if rgb_sep[k] > 255
                {
                    rgb_sep[k] = 255;
                }
            }

            // Update pixel values in array.
            image[i][j].rgbtRed = r_sepia;
            image[i][j].rgbtGreen = g_sepia;
            image[i][j].rgbtBlue = b_sepia;
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
