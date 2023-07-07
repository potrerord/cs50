"""
Write a function named print_powers_of_2 that accepts an integer >= 0
and prints each power of 2 from 2^0 (which is equal to 1) up to that
maximum power, inclusive.

For example, print_powers_of_2(10) should print

1 2 4 8 16 32 64 128 256 512 1024

print_powers_of_2(31) should print

        1 2 4 8 16 32 64 128 256 512 1024 2048 4096 8192
        16384 32768 65536 131072 262144 524288 1048576 2097152
        4194304 8388608 16777216 33554432 67108864 134217728
        268435456 536870912 1073741824 2147483648

You cannot make use of any Python functions or operators that compute
powers, such as ** or math.pow(). Write and use a main function that
demonstrates your function in action.
"""

def main():
    print_powers_of_2(arg1, arg2)


def print_powers_of_2(integer):
    if integer < 0:
        print("error: arg for print_powers_of_2() must be >= 0")
        return

    for i in range(10):
        print()






main()
