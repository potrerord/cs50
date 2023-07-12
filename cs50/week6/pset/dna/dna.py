"""
Identifies the likely source of a sequence of DNA.
"""


import csv
import sys


def main():
    """Load files from cmd-line argument and report if a DNA match is
    present.
    """

    # Check for command-line usage.
    if len(sys.argv) != 3:
        sys.exit("usage: python dna.py data.csv sequences.txt")

    # Read database file into a variable.
    with open(sys.argv[1], "r") as database, open(sys.argv[2], "r") as sequence_file:
        # Load database and sequence into memory.
        reader = csv.DictReader(database)
        sequence = sequence_file.read()

        # For every person in the database,
        for row in reader:
            # Initialize flag to break both loops if no match is found.
            break_loop = False

            # Create dictionary of STR counts.
            str_counts = list(row.items())[1:]

            # Compare STR count data with the return value of
            # longest_match for every subsequence for this person.
            for subsequence, str_count in str_counts:
                # Break if any comparison is not a match.
                if int(str_count) != longest_match(sequence, subsequence):
                    break_loop = True
                    break

            # Flag outer loop reset if no match was found.
            if break_loop:
                continue

            # If every STR count is a match, print the person's name.
            print(row["name"])
            return

        # If no match was found, print the result and return 1.
        print("No match")
        return 1


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
