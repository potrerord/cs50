"""
Computes the date of Easter Sunday in a given year that is provided by
user input. Uses formula developed by Carl Friedrich Gauss in 1800.
"""


def main():
    """Prompt for a year, calculate Easter date for that year, and print
    result.
    """

    # The variables correspond with the Gauss Easter date calculation
    # formula - Easter falls on day p of month n.
    y = int(input("\nEnter a year: "))

    a = y % 19
    b = y // 100
    c = y % 100
    d = b // 4
    e = b % 4
    g = (8 * b + 13) // 25
    h = (19 * a + b - d - g + 15) % 30
    j = c // 4
    k = c % 4
    m = (a + 11 * h) // 319
    r = (2 * e + 2 * j - k - h + m + 32) % 7
    n = (h - m + r + 90) // 25
    p = (h - m + r + n + 19) % 32

    # Print date in month/day format.
    print(f"{n}/{p}")
    print()


main()
