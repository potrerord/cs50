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

    # Number of medals.
    MEDAL_AMOUNT = 3

    # Predetermined ordered list of column headers.
    COLUMN_HEADERS = ["", "Gold", "Silver", "Bronze", "Total"]

    # Get maximum country length
    max_country_len = 0
    for country in medal_counts:
        if len(country) > max_country_len:
            max_country_len = len(country)

    # Initialize column_lengths dictionary with length of country column.
    column_widths = {"": max_country_len + SPACING}

    # Add other column widths to dictionary.
    for column in COLUMN_HEADERS[1:]:
        column_widths[column] = len(column) + SPACING

    # Alphabetize country keys from argument dictionary.
    sorted_countries = sorted(medal_counts)

    # Print first row with headers.
    for header in COLUMN_HEADERS:
        print(f"{header:>{column_widths[header]}}", end="")
    print()

    # Print remaining rows with data.
    for country in sorted_countries:

        # Print first column in each row.
        print(f"{country:>{max_country_len + SPACING}}", end="")

        # Print Gold.
        print(f"{medal_counts[country][0]:{column_widths['Gold']}}", end="")

        # Print Silver.
        print(f"{medal_counts[country][1]:{column_widths['Silver']}}", end="")

        # Print Bronze.
        print(f"{medal_counts[country][2]:{column_widths['Bronze']}}", end="")

        # Print total.
        total = sum(medal_counts[country])
        print(f"{total:>{column_widths['Total']}}", end="")
        print()




if __name__ == "__main__":
    main()
