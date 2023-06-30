"""
Prompts user for a number of students enrolled in a class, then
calculates and prints the number of teaching assistants necessary for
the class. Uses a ratio of 1 TA for every 15 students, rounded down.
"""


def main():
    """Prompt and calculate."""
    studs = int(input("How many students are enrolled? "))
    print ("We need", studs // 15, "teaching assistants")


main()