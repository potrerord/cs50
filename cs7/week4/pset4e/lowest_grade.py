"""
Removes the lowest score from a list of scores.
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
