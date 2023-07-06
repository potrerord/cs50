#include "helpers.h"
#include <math.h>


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
            gray_avg = (int)round(((r_orig + g_orig + b_orig) / 3.0));

            // Update image pixels with gray values.
            image[px_row][px_col].rgbtRed = gray_avg;
            image[px_row][px_col].rgbtGreen = gray_avg;
            image[px_row][px_col].rgbtBlue = gray_avg;
        }
    }

    return;
}

// Reflect image horizontally.
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // Make buffer variable to store pixels being moved.
    RGBTRIPLE buffer;
    int right_px;

    // Iterate over all rows.
    for (int px_row = 0; px_row < height; px_row++)
    {

        // Stop iteration within each row at halfway point.
        for (int left_px = 0, half_width = width / 2; left_px < half_width;
             left_px++)
        {
            // Update the right_px value to match the left (zero-index).
            right_px = width - left_px - 1;

            // Switch left pixel with corresponding right pixel.
            buffer = image[px_row][left_px];
            image[px_row][left_px] = image[px_row][right_px];
            image[px_row][right_px] = buffer;
        }
    }

    return;
}

// Blur image.
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Make a copy of image file to reference pre-blur image data.
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    // Declare variables for loops.
    float r_sum;
    float g_sum;
    float b_sum;
    int count;
    int r_blur;
    int g_blur;
    int b_blur;

    // Iterate over every pixel in row px_row and column px_col.
    for (int px_row = 0; px_row < height; px_row++)
    {
        for (int px_col = 0; px_col < width; px_col++)
        {
            // Reset sums and count.
            r_sum = 0;
            g_sum = 0;
            b_sum = 0;
            count = 0;

            // Get values from surrounding pixels (3x3 square).
            for (int i = -1; i < 2; i++)
            {
                // Skip calculation if row would go out of range.
                if (px_row + i < 0 || px_row + i >= height)
                {
                    continue;
                }

                for (int j = -1; j < 2; j++)
                {
                    // Skip calculation if column would go out of range.
                    if (px_col + j < 0 || px_col + j >= width)
                    {
                        continue;
                    }

                    // Add values to sums and increment count variable.
                    r_sum += (float)copy[px_row + i][px_col + j].rgbtRed;
                    g_sum += (float)copy[px_row + i][px_col + j].rgbtGreen;
                    b_sum += (float)copy[px_row + i][px_col + j].rgbtBlue;
                    count++;
                }
            }

            // Calculate avg of summed pixels rounded to nearest int.
            r_blur = (int)round((r_sum / count));
            g_blur = (int)round((g_sum / count));
            b_blur = (int)round((b_sum / count));

            // Update image pixels with blur values.
            image[px_row][px_col].rgbtRed = r_blur;
            image[px_row][px_col].rgbtGreen = g_blur;
            image[px_row][px_col].rgbtBlue = b_blur;
        }
    }

    return;
}


// Cap a double at a maximum.
double cap(double num, double max)
{
    if (num > max)
    {
        return max;
    }

    return num;
}


// Detect edges.
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    // Number of RGB values.
    const int RGB_VALUES = 3;

    // Number of squares in 3x3 grid.
    const int GRID_VALUES = 3;

    // Maximum color value.
    const int MAX_COLOR = 255;

    // Constants for notating R/G/B iteratively.
    const int R = 0;
    const int G = 1;
    const int B = 2;

    // Sobel operator kernels.
    const float GX_KERNEL[3][3] =
    {
        {-1, 0, 1},
        {-2, 0, 2},
        {-1, 0, 1}
    };

    const float GY_KERNEL[3][3] =
    {
        {-1, -2, -1},
        { 0,  0,  0},
        { 1,  2,  1}
    };

    // Make a copy of image file to reference original image data.
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    // Declare variables for loops.
    float r_sum_gx;
    float g_sum_gx;
    float b_sum_gx;
    float r_sum_gy;
    float g_sum_gy;
    float b_sum_gy;
    int count;
    double r_sobel_raw;
    double g_sobel_raw;
    double b_sobel_raw;
    int r_sobel;
    int g_sobel;
    int b_sobel;

    // Iterate over all pixels in row px_row and column px_col.
    for (int px_row = 0; px_row < height; px_row++)
    {
        for (int px_col = 0; px_col < width; px_col++)
        {
            // Reset sums.
            r_sum_gx = 0;
            g_sum_gx = 0;
            b_sum_gx = 0;
            r_sum_gy = 0;
            g_sum_gy = 0;
            b_sum_gy = 0;

            // Get values from surrounding pixels (3x3 square).
            for (int i = -1; i < 2; i++)
            {
                // Skip calculation if row would go out of range.
                if (px_row + i < 0 || px_row + i >= height)
                {
                    continue;
                }

                for (int j = -1; j < 2; j++)
                {
                    // Skip calculation if column would go out of range.
                    if (px_col + j < 0 || px_col + j >= width)
                    {
                        continue;
                    }

                    // Gx: Add values to sums.
                    r_sum_gx += (float)(copy[px_row + i][px_col + j].rgbtRed
                                        * GX_KERNEL[i + 1][j + 1]);
                    g_sum_gx += (float)(copy[px_row + i][px_col + j].rgbtGreen
                                        * GX_KERNEL[i + 1][j + 1]);
                    b_sum_gx += (float)(copy[px_row + i][px_col + j].rgbtBlue
                                        * GX_KERNEL[i + 1][j + 1]);

                    // Gy: Add values to sums.
                    r_sum_gy += (float)(copy[px_row + i][px_col + j].rgbtRed
                                        * GY_KERNEL[i + 1][j + 1]);
                    g_sum_gy += (float)(copy[px_row + i][px_col + j].rgbtGreen
                                        * GY_KERNEL[i + 1][j + 1]);
                    b_sum_gy += (float)(copy[px_row + i][px_col + j].rgbtBlue
                                        * GY_KERNEL[i + 1][j + 1]);
                }
            }

            // Calculate raw Sobel values.
            r_sobel_raw = sqrt(pow(r_sum_gx, 2) + pow(r_sum_gy, 2));
            g_sobel_raw = sqrt(pow(g_sum_gx, 2) + pow(g_sum_gy, 2));
            b_sobel_raw = sqrt(pow(b_sum_gx, 2) + pow(b_sum_gy, 2));


            // Calculate Sobel values rounded to nearest int and capped.
            r_sobel = (int)cap(round(r_sobel_raw), MAX_COLOR);
            g_sobel = (int)cap(round(g_sobel_raw), MAX_COLOR);
            b_sobel = (int)cap(round(b_sobel_raw), MAX_COLOR);

            // Update image pixels with Sobel values.
            image[px_row][px_col].rgbtRed = r_sobel;
            image[px_row][px_col].rgbtGreen = g_sobel;
            image[px_row][px_col].rgbtBlue = b_sobel;
        }
    }

    return;
}
