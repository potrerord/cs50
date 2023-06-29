# Outputs the sum of all even integers from 2 through user input int.

n = int(input("I will compute the sum of even integers from 2 through? "))
sum = 0

for even in range(2, n + 1, 2):
    