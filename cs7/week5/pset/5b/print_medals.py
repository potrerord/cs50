"""
Add your solution to the problem 'print_medals' here."""


def main():
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
    print(list(MEDAL_COUNTS))


def print_medals(medal_counts):
    """Take the a dictionary of medal counts and prints
    a nicely formatted table with totals for each country
    as described in the pset 5 problem.
    """
    # Add your code here.


if __name__ == "__main__":
    main()
