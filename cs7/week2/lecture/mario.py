## Prints a mario half pyramid of user-input size

n = int(input("Enter size: "))

## Print n rows
for i in range (n):

    ## Print decreasing spaces
    for j in range (n - i):
        print(" ", end = "")

    ## Print increasing #
    for j in range (i + 1):
        print("#", end = "")
    print()