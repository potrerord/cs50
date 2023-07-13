"""
Following along with Week 7.

favorites.csv data:
timestamp,language,problem
"""


import csv


def main():
    """Mess with the data of favorite CS50 problems."""

    with open("favorites.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row[1])


if __name__ == "__main__":
    main()
