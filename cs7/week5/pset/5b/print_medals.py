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

    print_medals(MEDAL_COUNTS)




def print_medals(medal_counts):
    """Take the a dictionary of medal counts and prints
    a nicely formatted table with totals for each country
    as described in the pset 5 problem.
    """

    # Predetermined ordered list of column headers.
    COLUMN_HEADERS = ["", "Gold", "Silver", "Bronze", "Total"]

    sorted_countries = sorted(medal_counts)

    for country in sorted_countries:




if __name__ == "__main__":
    main()
