"""
Prints a sequential list of all integers between a defined start and end
(inclusive).
"""


def main():
   """Take user input and call print_range function."""

   print()
   user_start = (int(input("Enter a starting value: ")))
   user_range = (int(input("Enter an ending value:  ")))
   print_range(user_start, user_range)
   print()


def print_range(start: int, end: int):
   """Print a sequential list of all integers between a defined start and end
   (inclusive).
   """

   if isinstance(start, int) or isinstance(end, int):
      print("error: start and end must be integers")
      return

   # Print opening tag.
   print(f"[{start},{end}]: ", end="")

   # Define the limit for the range of printed integers.
   if start <= end:
      print_end = end + 1
   else:
      print_end = end - 1

   # Print list of integers.
   for i in range(start, print_end):

      # Print final value without comma and with new line.
      if i == print_end:
         print(f"{i}")
      else:
         print(f"{i}, ", end="")


main()
