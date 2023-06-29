# 12345678901234567890123456789012345678901234567890123456789012345678901234567

"""
I have been told that there are a few 3-digit integers that are equal to the
sum of the cube of their individual digits. Find all of them, and print them
out!
"""

# Prints all 3-digit integers equal to the sum of the cube of their digits

for n in range(100, 1000):
    a = n // 100 % 10
    b = n // 10 % 10
    c = n % 10

    cubesum = a**3 + b**3 + c**3

    if cubesum == n:
        print(cubesum)

    n += 1
