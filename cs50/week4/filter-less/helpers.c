#include "helpers.h"
#include <math.h>


// Global constant for number of RGB values.
const int RGB_VALUES = 3;


// Convert image to grayscale.
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // Create variables for color values.
    int r_orig;
    int g_orig;
    int b_orig;
    int gray_avg;

    // Iterate over all pixels in row px_row and column px_col.
    for (int px_row = 0; px_row < height; px_row++)
    {
        for (int px_col = 0; px_col < width; px_col++)
        {
            // Store R/G/B values for the pixel.
            r_orig = image[px_row][px_col].rgbtRed;
            g_orig = image[px_row][px_col].rgbtGreen;
            b_orig = image[px_row][px_col].rgbtBlue;

            // Take average of R/G/B values, rounded to the nearest int.
            gray_avg = (int) round(((r_orig + g_orig + b_orig) / 3.0));

            // Update pixel values in array.
            image[px_row][px_col].rgbtRed = gray_avg;
            image[px_row][px_col].rgbtGreen = gray_avg;
            image[px_row][px_col].rgbtBlue = gray_avg;
        }
    }

    return;
}


// Convert image to sepia.
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    // Create constant sepia conversion factors. Multiply each original
    // R/G/B value by the respective factors in each row to get the
    // corresponding sepia value for that row's color.
    float CONV_FACTORS[RGB_VALUES][RGB_VALUES] = {
        {0.393, 0.769, 0.189},  // Row 0: RED;   Columns: R, G, B
        {0.349, 0.686, 0.168},  // Row 1: GREEN; Columns: R, G, B
        {0.272, 0.534, 0.131}   // Row 2: BLUE;  Columns: R, G, B
    };


    // Create variables to store color values
    int orig[RGB_VALUES];

    // Iterate over all pixels in row px_row and column px_col.
    for (int px_row = 0; px_row < height; px_row++)
    {
        for (int px_col = 0; px_col < width; px_col++)
        {
            // Store R/G/B values for the pixel in orig array.
            orig = {
                image[px_row][px_col].rgbtRed,
                image[px_row][px_col].rgbtGreen,
                image[px_row][px_col].rgbtBlue
            };

            // Initialize all sepia values to 0.0 for conversion sum.
            float sepia[RGB_VALUES] = {0.0};

            // Convert to sepia using conv_factors row/col structure.
            for (int rgb_row = 0; rgb_row < RGB_VALUES; rgb_row++)
            {
                for (int rgb_col = 0; rgb_col < RGB_VALUES; rgb_col++)
                {
                    // Compute sepia values by adding respective
                    // conversion products.
                    sepia[rgb_row] += (CONV_FACTORS[rgb_row][rgb_col] *
                                       orig[rgb_col]);
                }

                // Cap each converted sepia value at 255.
                if (sepia[rgb_row] > 255)
                {
                    sepia[rgb_row] = 255;
                }
            }

            // Update pixel values in array.
            image[px_row][px_col].rgbtRed = sepia[0];
            image[px_row][px_col].rgbtGreen = sepia[1];
            image[px_row][px_col].rgbtBlue = sepia[2];
        }
    }

    return;
}


// Reflect image horizontally.
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // Make buffer variable to store pixels being moved.
    int buffer;
    int right_px;

    // Iterate over all rows.
    for (int px_row = 0; px_row < height; px_row++)
    {

        // Stop iteration within each row at halfway point.
        for (int left_px = 0, int half_width = width / 2; left_px < half_width; left_px++)
        {
            // Update the right_px value to match the left, subtracting
            // 1 to account for zero-index.
            right_px = width - left_px - 1;

            // Switch left pixel with corresponding right pixel
            buffer = image[px_row][left_px];
            image[px_row][left_px] = image[px_row][right_px];
            image[px_row][right_px] = buffer;
        }
    }

    return;
}


// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{



    return;
}
