"""
I have been told that there are a few 3-digit integers that are equal to the
sum of the cube of their individual digits. Find all of them, and print them
out!
"""

# Prints all 3-digit integers equal to the sum of the cube of their digits

# Start at 100, go to 999
for n in range(100, 1000):
    a = n // 100 % 10
    b = n // 10 % 10
    c = n % 10

    # Print if sum of digits' cubes equals n
    if n == a**3 + b**3 + c**3:
        print(n)

    # Increment to next 3 digit integer
    n += 1