## Prints mario half pyramid in a Pythonic way

## Prompt user for size of half pyramid
n = int(input("Enter size: "))

## Print n rows, start with row 1 to simiplify calculations
for row in range (1, n + 1):

    ## Print decreasing spaces
    print(' ' * (n - row), end = '')

    ## Print increasing #; number matches row number
    print('#' * row, end = '')

    ## Single newline at end of each row
    print()