"""Add your solution to the problem 'authorship' here."""


import romeo_and_juliet_data


def main():
    # Add your solution to the problem that makes use of the above to
    # print out the word length frequency table described in the pset.

    rj_histogram, rj_total_words = word_length_histogram(romeo_and_juliet_data.lines)

    sorted_rj_histogram = 

    for length in rj_histogram:



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

    # Eliminate apostrophes.
    text = text.replace("'", "")

    histogram = {}
    total_words = 0
    for line in text:
        for word in line.split():
            # Initialize new word length if it doesn't exist.
            if not histogram[len(word)]:
                histogram[len(word)] = 0

            # Increment word count.
            histogram[len(word)] += 1
            total_words += 1

    return histogram, total_words


if __name__ == "__main__":
    main()
