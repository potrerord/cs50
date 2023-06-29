## Prints mario half pyramid in a Pythonic way

n = int(input("Enter size: "))

for i in range (1, n + 1):
    print(' ' * (n - i))
    print('#' * i)
    print()