"""Add your solution to the problem 'authorship' here."""


import romeo_and_juliet_data


def main():
    # Add your solution to the problem that makes use of the above to
    # print out the word length frequency table described in the pset.

    print()

    # Test on Romeo and Juliet.
    rj_histogram, rj_total_words = word_length_histogram(romeo_and_juliet_data.lines)

    # Make sorted list of histogram keys.
    sorted_rj_histogram = sorted(rj_histogram.keys())

    # Iterate through sorted key list.
    for word_length in sorted_rj_histogram:
        # Calculate proportion.
        proportion = rj_histogram[word_length] / rj_total_words * 100

        # Format proportion as percentage rounded to 2 decimals.
        proportion = f"{round(proportion, 2):.2f}"

        # Print report for user.
        print(f"Proportion of {word_length}-letter words: {proportion}% "
              f"({rj_histogram[word_length]} words)")

    print()


def word_length_histogram(text):
    """Takes the a list of multiword lines and returns
    a dictionary where the keys are word lengths and the
    values are how many words there are of that length.
    Assume there is no punctuation to worry about.
    For example, the input:
        [ "Summer school", "is nearly over"]
    should return the dictionary
        { 6 : 3, 2 : 1, 4 : 1 }
    """

    histogram = {}
    total_words = 0
    for line in text:
        # Eliminate apostrophes.
        line = line.replace("'", "")

        for word in line.split():
            # Initialize new word length if it doesn't exist.
            if len(word) not in histogram:
                histogram[len(word)] = 0

            # Increment word count.
            histogram[len(word)] += 1
            total_words += 1

    return histogram, total_words


if __name__ == "__main__":
    main()
