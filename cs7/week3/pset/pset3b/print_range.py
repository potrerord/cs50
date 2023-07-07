"""
Prints a sequential list of all integers between a defined start and end
(inclusive).
"""

"""
Write a function named print_range that accepts two integers i, j as
arguments and prints the sequence of numbers between the two arguments,
prefixed with the string "[i,j]:". Print an increasing sequence if the
first argument is smaller than the second; otherwise, print a decreasing
sequence. If the two arguments are the same, just that number should be
printed. Here are some sample calls to print_range:
   print_range(2, 7)
   print_range(19, 11)
   print_range(5, 5)
The output produced from these calls should be the following sequences:
   [2,7]: 2, 3, 4, 5, 6, 7
   [19,11]: 19, 18, 17, 16, 15, 14, 13, 12, 11
   [5,5]: 5

Your function should be tested out using a main function of your own design.
"""


def main():
    print_range()


def print_range(start: int, end: int):
   """Prints a sequential list of all integers between a defined start and end
   (inclusive).
   """

   # Print opening tag.
   print(f"[{start},{end}]: ", end="")

   # Define the limit for the range of printed integers.
   if start <= end:
      print_end = end + 1
   else:
      print_end = end - 1

   # Print list of integers.
   for i in range(start, print_end):

      if i == start:
         print(f"{i}")
      # Make sure it starts/ends with or without a comma


      # Make sure it prints range + 1 to get end in there

      print(f"{i}, ", end="")
   print()






main()
