"""
Following along with Week 7.

favorites.csv data:
timestamp,language,problem
"""


import csv


def main():
    """Mess with the data of favorite CS50 problems."""

    with open("favorites.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            favorite = row["language"]
            print(favorite)


if __name__ == "__main__":
    main()
