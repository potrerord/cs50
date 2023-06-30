# Prints a box with user-input size.

size = int(input("Enter a size: "))

# Range starts at 1 to use row number in calculations.
for row in range(1, size + 1):
    if (row = 1):
        
    print("+")
# First row always prints +, then n -, then +
# Middle rows always print |, then n " ", then |
# Last row prints first row