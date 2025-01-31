"""Add your solution to the problem 'courses' here."""


def main():
    # Add your solution to the problem that makes use of the above.
    COURSES = {
        "CSCI-S7": {
            "full_name":     "Intro to CS with Python",
            "instructors":   ["Henry", "Dimitri"],
            "tfs":           ["Alyssa", "Apekshya", "Ben", "Devon", "Nabib",
                              "Nicholas", "Omar", "Thomas",],
            "num_homeworks": 6,
            "num_exams":     2,
        },
        "FREN-SAA": {
            "full_name":     "Beginning French I",
            "instructors":   ["Elodie"],
            "tfs":           ["Gloria", "Mona"],
            "num_homeworks": 12,
            "num_exams":     2,
        },
    }
    print("total_homeworks: ", total_homeworks(COURSES))
    print("total_homeworks2: ", total_homeworks2(COURSES))


def total_homeworks(courses):
    """Takes the a dictionary of courses as students is taking
    and returns the total number of homeworks they have.
    Must use a for loop
    """

    sum = 0
    for course in courses:
        sum += courses[course]["num_homeworks"]
    return sum


def total_homeworks2(courses):
    """Takes the a dictionary of courses as students is taking
    and returns the total number of homeworks they have.
    Must use a list comprehension and sum.
    """

    return sum([courses[course]["num_homeworks"] for course in courses])


if __name__ == "__main__":
    main()
