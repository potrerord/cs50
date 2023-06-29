## Prints mario half pyramid in a Pythonic way

## Prompt user for size of half pyramid
n = int(input("Enter size: "))

## Print n rows
for i in range (1, n + 1):

    ## Print decreasing spaces
    print(' ' * (n - i), end = '')

    ## Print increasing # - number matches row number
    print('#' * i, end = '')

    ## Single newline at end of each row
    print()