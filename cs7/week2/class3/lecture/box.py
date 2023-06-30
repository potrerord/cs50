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
        mid_char = " "

    print(end_char + mid_char * (size - 2) + end_char)