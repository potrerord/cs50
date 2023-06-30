# Prints a box with user-input size.

size = int(input("Enter a size: "))

# Range starts at 1 to use row number in calculations.
for row in range(1, size + 1):

    # Define end/middle characters depending on row.
    if(row == 1 or row == size):
        end_char = "+"
        mid_char = "-"
    else:
        end_char = "|"
        mid_char = "|"

    print(end_char)

    # Print first character.


    # Print middle characters.


    # Print last character.

    # Prints +--+ for first/last rows.
    if(row == 1 or row == size):
        print("+", end="")
        print("-" * (size - 1), end="")
        print("+")

    # Prints |  | for middle rows.
    else:
        print("|", end="")
        print(" " )
# First row always prints +, then n -, then +
# Middle rows always print |, then n " ", then |
# Last row prints first row