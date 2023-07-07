"""
Write a Python program to compute the largest absolute change that
occurred in the price of a stock during a 10-day period. The program
should prompt the user 10 times for integers representing the stock
price on 10 consecutive days. If the integers input were

   48  54  49  47  62  84  59  70  75  82

then the program should print a message like

   Largest change of 25 from  84  to  59 occurred between day #6 and day
   #7.

Your program must implement and use the following two functions

   def print_change(day1_price, day2_price, day1_num):
       ...

   def find_change():
       ...

The function print_change should take the prices on the two days and the
number of the initial day of the change and print out the message. The
function find_change should take no parameters, prompt the user for the
stock prices and return a list with the prices on the two days, and the
number of the initial day of the change. Other than the user prompts,
find_change should not print anything out. Your main function should use
the functions find_change and print_change to execute the program.

You must design your program in such a way that you do not have to save
all the prices in memory before computing the answer. As well, modifying
the total number of days from 10 to 30 (for example) should merely
require updating one variable. You are not allowed to use any list,
tuple, string variables in this problem other than the return value of
find_change, which is a list. You are also not allowed to use 10
variables to store the prices. You will get no credit for such a
solution.
"""

"""
Computes and prints the largest absolute daily change in the price of a
stock during a 10-day period.
"""


from typing import List



# Implement a main function that computes the largest change as
# specified in problem 12, by using find_change to find the largest
# change and print_change to print the final answer.
def main():
    """Compute the largest change and print final answer."""

    # Prompt user for prices and find largest change.
    find_change()

    # Print answer.
    print_change()


# Implement a function find_change that prompts the user for the
# appropriate number of stock prices and returns a list with the the
# value on the first day, the value on the second day, and the number
# of the first day, in that order.

def find_change() -> List[int]:
    """Prompt the user for the appropriate number of stock prices and
    return a list containing the values on the first and second days,
    then the first day's number.
    """

    # Constant: Number of days of price data to request from user.
    DAY_COUNT = 10

    
    


    input()
    return list[]


# Implement a function print_change that takes in the results of your
# computation and prints them out in a message for the user.

# For example:
# Largest change of 25 from 84 to 59 occurred between day #6 and day #7.

# Must not prompt the user for anything.
def print_change(day1_price, day2_price, day1_num):
    *** add your code here ***


# Run the main function if script is run directly.
if __name__ == "__main__":
    main()
