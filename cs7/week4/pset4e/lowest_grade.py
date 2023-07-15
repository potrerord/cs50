"""
It is common in some courses (though not in CSCI-S7) for an instructor
to not count the lowest exam score or homework score for each student.

Define a function named remove_lowest that accepts a list of numbers
that represent the homework scores of a single student.

Your function should return a list that contains all of the values
passed to the function EXCEPT for the lowest score. Your function should
not modify the original list. To illustrate how this function ought to
work, consider the following code:

    x = [23, 90, 47, 55, 88]
    a = remove_lowest(x)
    b = remove_lowest([85])
    c = remove_lowest([])
    d = remove_lowest([59, 92, 93, 47, 88, 47])
    print("x =", x)
    print("a =", a)
    print("b =", b)
    print("c =", c)
    print("d =", d)

The correct output would be

    x = [23, 90, 47, 55, 88]
    a = [90, 47, 55, 88]
    b = [85]
    c = []
    d = [59, 92, 93, 88, 47]

Note that in the case of a, the lowest score, 23, was removed.

The fourth case, d, shows what happens when the lowest score appears
twice: it is removed only once from the list that is constructed.
"""


from typing import List


def main():
    """Run remove_lowest with test input."""

    # Constant test grades.
    TEST1 = [23, 90, 47, 55, 88]
    TEST2 = [85]
    TEST3 = []
    TEST4 = [59, 92, 93, 47, 88, 47]

    # Test code.
    a = remove_lowest(TEST1)
    b = remove_lowest(TEST2)
    c = remove_lowest(TEST3)
    d = remove_lowest(TEST4)

    # Print tests.
    print("a =", a)
    print("b =", b)
    print("c =", c)
    print("d =", d)


def remove_lowest(grade_list: List[int]) -> List[int]:
    """Returns a new list with the lowest score removed if there are at
    least two grades in the original list.
    """

    # Immediately return original list if it is not long enough.
    if len(grade_list) < 2:
        return grade_list

    # Copy list into new list.
    new_list = grade_list

    # Remove lowest value from new list.
    lowest_grade = min(new_list)
    new_list.remove(lowest_grade)

    return new_list




if __name__ == "__main__":
    main()
