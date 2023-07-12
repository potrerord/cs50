"""
# 1a.
for i in range(5):
    print(i)

01234

# 1b.
for i in range(0, 30, 3):
    print(i)

0 3 6 9 12 15 18 21 24 27

# 1c.
for i in range(30, 6, -3):
    print(i)

30 27 24 21 18 15 12 9

# 1d.
# Write a program that randomly generates numbers in the range [1,10]
# and prints them, until it generates a 6, at which point it prints it
# and stops.
"""


import random


def main():
    random_number = random.randint(1, 10)
    while True:
        print(random_number)
        if random_number == 6:
            return


if __name__ == "__main__":
    main()
