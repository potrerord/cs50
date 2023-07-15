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

    #add a person
    name = get_string("Name: ")
    student_id = database.execute("INSERT INTO people (name) VALUES (?)", name)

    #prompt for courses to enroll in
    while True:
        code = get_string("Course code: ")

        #if no input, then stop adding - TODO
        if code == "":
            sys.exit(1)

        #query for course - TODO
        course = database.execute("SELECT id, code FROM courses;")

        #check to make sure course exists - TODO
        flag = False
        for course_info in course:
            if course_info[code] == code:
                flag = True
        if not(flag):
            sys.exit(1)

        #enroll student - TODO
        database.execute("INSERT INTO students (person_id, course_id) \
                         VALUES(SELECT id FROM people WHERE name = ?", name))

if __name__ == "__main__":
    main()