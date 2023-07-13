"""
Following along with Week 7.

favorites.csv data:
timestamp,language,problem
"""


import csv


def main():
    """Mess with the data of favorite CS50 problems."""

    # Open/close file.
    with open("favorites.csv", "r") as file:
        reader = csv.DictReader(file)
        scratch, c, python = 0, 0, 0
        for row in reader:
            favorite = row["language"]
            if favorite == "scratch":
                scratch += 1
            elif favorite == "c":
                c += 1
            elif favorite == "python":
                python += 1


    # Print.
    print(f"{scratch>7}: {scratch}")
    print()


if __name__ == "__main__":
    main()
