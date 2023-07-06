"""
The proper divisors of an integer n are the positive divisors less than
n. A positive integer is said to be a deficient, perfect, or abundant
number if the sum of its proper divisors is less than, equal to, or
greater than the number, respectively.

For example,
8 is deficient,
    because its proper divisors are 1, 2 and 4, and 1+2+4 < 8;
6 is perfect,
    because 1+2+3 = 6;
12 is abundant,
    because 1+2+3+4+6 > 12.

Write a Python program that accepts two positive integer values that are
input by the user running the program (say m and n, where m <= n) and
prints deficient, perfect or abundant for each value between m and n
inclusive. Your program must implement a function

def divisors(n):
    ...

The function must return (not print!) deficient, perfect or abundant for
a given number. You may want to Google for examples of perfect numbers
to be sure your function is behaving correctly. The output from your
main program will look something like this:

Please input an integer value for m: 5
Now input an integer value for n that is greater than or equal to 5: 31
   5 is deficient
   6 is perfect
   7 is deficient
...

"""
# Returns 'deficient', 'perfect', or 'abundant' for
# for the number n, as specified in the problem set.
#
# Must not print anything out.
def divisors(n):
    *** add your code here ***

# Add a main function that prompts the user for two numbers and
# calls divisors as instructed in the problem description.
def main():
    *** add your code here ***

# Runs the main function. Leave as is.
if __name__ == "__main__":
    main()
