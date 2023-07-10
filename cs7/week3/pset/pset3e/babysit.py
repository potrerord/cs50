"""
Write a Python program that calculates how much to pay the babysitter.
Although the problem sounds simple, it's trickier than it appears. Read
on carefully!

Assume that the starting time for the babysitter is somewhere between
6 PM and 11 PM (inclusive); and that the ending-time is somewhere
between 9 PM and 4 AM (inclusive).

The only input to your program will be 4 numbers.

The starting time is expressed as hours and minutes, and the ending time
is also expressed as hours and minutes.

For example, if the baby sitter works from 7:45 PM until 1:12 AM, then
the input to your program should look like the following:

At what HOUR did the babysitter start work? 7
At what MINUTE did the babysitter start work? 45
At what HOUR did the babysitter finish working? 1
At what MINUTE did the babysitter finish working? 12

... ... ...
No other form of input is acceptable! Also, no other information can be
input to the program.

The output from your program should be the amount of money to be paid to
the babysitter. The pay scale is: $18.00 per hour for 6 PM until 8 PM;
$25.00 per hour from 8 PM until midnight; and $30.00 an hour after
midnight. Use variables for these three pay scales.
Your program should validate user input. If the user types input values
that either are outside of the allowable range of possible working
hours, or if the starting time is later than the ending time — then your
program should print an appropriate error message, and exit.

Your program must implement a function

def babysit(start_hour, start_min, end_hour, end_min):
    ...

that takes the starting and end time as input and returns (and doesn't
print!) the amount of money owed to the babysitter.
"""

# Takes in the starting and ending times for the babysitter and returns
# the amount of money owed to them.
#
# Must not print anything out.
def babysit(start_hour, start_min, end_hour, end_min):
    *** your code goes here ***

# Add a main function that prompts the user for the start and end
# times, calls babysit and prints the amount owed as instructed in the
# problem description.
def main():
    *** add your code here ***

# Run the main function if script is run directly.
if __name__ == "__main__":
    main()
