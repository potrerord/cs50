"""
Computes and prints the largest absolute daily change in the price of a
stock during a 10-day period.
"""

from typing import List


def main():
    """Compute the largest change and print final answer."""

    # Prompt user for prices and find largest change.
    print()
    change_info = find_change()
    print()

    # Print largest change.
    print()
    print_change(change_info[0], change_info[1], change_info[2])
    print()


def find_change() -> List[int]:
    """Prompt the user for the appropriate number of stock prices and
    return a list containing the values on the first and second days,
    then the first day's number.
    """

    # Constant: Number of days of price data to request from user.
    DAY_COUNT = 10

    # Create tracker variables.
    largest_change = 0
    start_price = 0
    end_price = 0
    saved_start = 0
    saved_end = 0
    start_day = 0

    for day in range(1, DAY_COUNT + 1):

        # Assign end price to start price before overwriting.
        start_price = int(end_price)

        # Get user input for new end price.
        end_price = int(input(f"Enter the Day {day} price: "))

        if day > 1:
            change = int(abs(end_price - start_price))

            # If current change is largest, update variables.
            if change > largest_change:
                saved_start = start_price
                saved_end = end_price
                largest_change = change
                start_day = day - 1

    change_info = [int(saved_start), int(saved_end), int(start_day)]
    return change_info


def print_change(day1_price: int, day2_price: int, day1_num: int) -> None:
    """Print report to terminal."""

    print(f"The largest change was ${abs(day2_price - day1_price)} from "
          f"${day1_price} to ${day2_price}, occurring between Day #{day1_num} "
          f"and Day #{day1_num + 1}.""")


# Run the main function if script is run directly.
if __name__ == "__main__":
    main()
