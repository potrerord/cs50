"""
Write a Python program enroll.py to add new students to the roster and
enroll them in courses.

Usage:
    $python3 enroll.py
    Name: Guy
    Course Code: ABCD
    No course with code ABCD
    Course Code: CS50
    Added Guy to CS50
"""


from cs50 import get_string, SQL
import sys


def main():

    database = SQL("sqlite:///students.db")

    # Add a person.
    name = get_string("Name: ")
    student_id = database.execute("INSERT INTO people (name) VALUES (?)", name)

    # Prompt for courses to enroll in.
    while True:
        code = get_string("Course code: ")

        # If no input, then stop adding.
        if not code:
            sys.exit(1)

        # Query for course.
        course_codes = database.execute("SELECT code FROM courses;")

        # Check to make sure course exists.
        if code not in course_codes:
            sys.exit(1)

        # Enroll student.
        database.execute("INSERT INTO students (person_id, course_id) VALUES(?, ?);", student_id, code)


if __name__ == "__main__":
    main()