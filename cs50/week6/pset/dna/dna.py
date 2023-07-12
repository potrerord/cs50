"""
Identifies the likely source of a sequence of DNA.
"""


import csv
import sys


def main():
    """butt"""

    # Check for command-line usage.
    if len(sys.argv) != 3:
        sys.exit("usage: python dna.py data.csv sequences.txt")

    # Read database file into a variable.
    with open(sys.argv[1], "r") as data, open(sys.argv[2], "r") as sequence:
        reader = csv.DictReader(data)

        # Create list of subsequences.
        subsequences = []
        for subsequence in reader.fieldnames[1:]:
            subsequences.append(subsequence)

        #
        for row in reader:
            str_counts = list(row.items())[1:]
            for fieldname, value in str_counts:
                if value != longest_match(sequence, fieldname):
                    break_loop




        for subsequence in reader.fieldnames[1:]:
            if longest_match(sequence, subsequence) ==



            for row in reader:
                if

        # TODO: Find longest match of each STR in DNA sequence
        butt = longest_match(sequence, subsequence)

        # TODO: Check database for matching profiles


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
