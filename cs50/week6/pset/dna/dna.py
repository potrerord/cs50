"""
Identifies the likely source of a sequence of DNA.
"""


import csv
import sys


def main():

    # Check for command-line usage.
    if len(sys.argv) != 3:
        sys.exit("usage: python dna.py data.csv sequences.txt")

    # Read database file into a variable.
    with open(sys.argv[1], "r") as database:
        reader = csv.DictReader(database)
        for row in reader:






    # TODO: Read DNA sequence file into a variable





    # TODO: Find longest match of each STR in DNA sequence





    # TODO: Check database for matching profiles





    return


def longest_match(sequence: str, subsequence: str) -> int:
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables.
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each char in sequence to count the highest number of
    # consecutive runs of subsequence.
    for i in range(sequence_length):

        # Initialize count of consecutive runs.
        count = 0

        # Check sequence substrings for a match with subsequence, move
        # substring to next potential match in sequence if successful,
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

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
