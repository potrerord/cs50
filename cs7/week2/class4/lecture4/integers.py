# I have been told that there are a few 3-digit integers that are equal to the sum of the cube of their individual digits. Find all of them, and print them out!

n = 0
while (n < 100 or n >999):
    n = int(input("Enter a 3-digit integer: "))

a = n // 100 % 10
b = n // 10 % 10
c = n % 10

cubesum = a ** 3 + b ** 3 