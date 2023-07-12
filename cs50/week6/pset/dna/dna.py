"""
Identifies a likely match for a sequence of DNA from a database of names
and STR counts, if a match exists.
"""


import csv
import sys
from typing import Dict


def main():
    """Load files from cmd-line argument and report if a DNA match is
    present.
    """

    # Check for command-line usage.
    if len(sys.argv) != 3:
        sys.exit("usage: python dna.py data.csv sequences.txt")

    # Read sequence file into a variable, then close file.
    with open(sys.argv[2], "r") as sequence_file:
        arg_sequence = sequence_file.read()

    # Open database file, close when check is complete.
    with open(sys.argv[1], "r") as database:
        # Create iterator object to read file row by row.
        reader = csv.DictReader(database)

        # Check each person in the database until a match is found.
        for row in reader:
            # If every STR run count matches, print the name and return.
            if find_match(row, arg_sequence):
                print(row["name"])
                return

    # If no match was found, print the result and return 1.
    print("No match")
    return 1


def find_match(data: Dict[str, str], sequence: str) -> bool:
    """Return bool indicating if data and sequence STR counts match.

    Arguments:
    data -- Dictionary list with "name" followed by longest STR counts
    sequence -- The DNA string to analyze and compare longest STR counts
    """

    # Compare the dictionary STR count data with the sequence STR count
    # for each subsequence. Omit name column.
    for subsequence, count in list(data.items())[1:]:
        # Return False if any comparison is not a match.
        if int(count) != longest_match(sequence, subsequence):
            return False

    # Return True if all STR counts match.
    return True


def longest_match(sequence: str, subsequence: str) -> int:
    """Return length of longest run of subsequence in sequence."""

    # Initialize variables.
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each char in sequence to count the highest number of
    # consecutive runs of subsequence.
    for i in range(sequence_length):
        # Initialize count of consecutive runs.
        count = 0

        # Check substrings of sequence for a match with subsequence,
        # move substring to next potential match in sequence if success,
        # and repeat until out of consecutive matches.
        while True:
            # Adjust substring start and end.
            start = i + count * subsequence_length
            end = start + subsequence_length

            # Increment if there is a match in the substring.
            if sequence[start:end] == subsequence:
                count += 1

            # Break if there is no match in the entire substring.
            else:
                break

        # Update the highest number of consecutive matches found.
        longest_run = max(longest_run, count)

    # Return longest run found after all characters are checked.
    return longest_run


if __name__ == "__main__":
    main()
