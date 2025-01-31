"""
Following along with Week 7.

favorites.csv data:
timestamp,language,problem
"""


import csv


def main():
    """Mess with the data of favorite CS50 problems."""

    # Open with newline.
    print()

    # Open/close file.
    with open("favorites.csv", "r") as file:
        reader = csv.DictReader(file)

        counts = {}

        for row in reader:
            favorite = row["language"]
            if favorite in counts:
                counts[favorite] += 1
            else:
                counts[favorite] = 1


    # Print.
    for favorite in sorted(counts, key=lambda favorite: counts[favorite],
                            reverse=True):
        print(f"{favorite:>7}: {counts[favorite]}")

    # Close with newline.
    print()


if __name__ == "__main__":
    main()
