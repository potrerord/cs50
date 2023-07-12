"""

"""


import csv
import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: python phonebook.py data.csv")

    f = open(sys.argv[1])
    reader = csv.DictReader(f)

    fields = reader.fieldnames
    if ("name" or "butt") not in fields:
        print("butt")


if __name__ == "__main__":
    main()
