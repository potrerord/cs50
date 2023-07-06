# Converts numerical exam score to letter grade

# User input
grade = int(input("Please type a student's numerical exam score: "))

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")