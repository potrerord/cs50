"""
Prints a sequential list of all integers between a defined start and end
values (inclusive).
"""


def main():
   """Take user input and call print_range function."""

   print()

   user_start = (int(input("Enter a starting value: ")))
   user_range = (int(input("Enter an ending value:  ")))

   print()

   print_range(user_start, user_range)

   print()


def print_range(start: int, end: int):
   """Print a sequential list of all integers between start and end
   arguments (inclusive).
   """

   # Print error if start or end are not integers.
   if not isinstance(start, int) or not isinstance(end, int):
      print("error: start and end must be integers")
      return

   # Print opening tag.
   print(f"[{start},{end}]: ", end="")

   # Define the limit for the range of printed integers.
   if start <= end:
      print_end = end + 1
      increment = 1
   else:
      print_end = end - 1
      increment = -1

   # Print list of integers.
   for i in range(start, print_end, increment):

      # Print first value without preceding comma.
      if i == start:
         print(f"{i}", end="")
      else:
         print(f", {i}", end="")

   # Print new line after final value.
   print()


# Run the main function if script is run directly.
if __name__ == "__main__":
    main()
