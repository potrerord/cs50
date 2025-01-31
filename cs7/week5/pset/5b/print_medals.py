"""
Prints a table of the number of medals won in the recent Winter Olympics
by country.
"""


def main():
    """Call function."""

    # Dictionary of Gold/Silver/Bronze medals by country.
    MEDAL_COUNTS = {
        "Canada": [0, 3, 0],
        "Italy": [0, 0, 1],
        "Germany": [0, 0, 1],
        "Japan": [1, 0, 0],
        "Kazakhstan": [0, 0, 1],
        "Russia": [3, 1, 1],
        "South Korea": [0, 1, 0],
        "United States": [1, 0, 1],
    }

    print()
    print_medals(MEDAL_COUNTS)
    print()


def print_medals(medal_counts):
    """Take the a dictionary of medal counts and prints
    a nicely formatted table with totals for each country
    as described in the pset 5 problem.
    """

    # Constant spacing between columns.
    SPACING = 2

    # Predetermined ordered list of column headers.
    HEADERS = ["", "Gold", "Silver", "Bronze", "Total"]

    # Get maximum country length
    max_country_len = 0
    for country in medal_counts:
        if len(country) > max_country_len:
            max_country_len = len(country)

    # Initialize column_lengths dictionary with length of country column.
    widths = {"": max_country_len + SPACING}

    # Add other column widths to dictionary.
    for column in HEADERS[1:]:
        widths[column] = len(column) + SPACING

    # Alphabetize country keys from argument dictionary.
    sorted_countries = sorted(medal_counts)

    # Print first row with headers.
    for header in HEADERS:
        print(f"{header:>{widths[header]}}", end="")
    print()

    # Print remaining rows with data.
    for country in sorted_countries:
        for col in range(len(HEADERS)):
            # Define column width for this column.
            column_width = widths[HEADERS[col]]

            # Print first column (country names).
            if col == 0:
                print(f"{country:>{column_width}}", end="")

            # Print medal data in order starting at second column.
            elif 0 < col < len(HEADERS) - 1:
                print(f"{medal_counts[country][col - 1]:>{column_width}}", end="")

            # Print final column (Total) with newline.
            else:
                print(f"{sum(medal_counts[country]):>{column_width}}", end="")
                print()


if __name__ == "__main__":
    main()
