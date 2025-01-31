"""
Given the time of day in terms of an hour, minute, second and whether it
is AM or PM, write a Python function named fraction_of_day to calculate
and return (not print!) the fraction of the day (a value of type float)
that has elapsed since midnight (12:00 AM). For example,

fraction_of_day(12, 0, 0, 'A')
would evaluate to 0.0

fraction_of_day(12, 0, 0, 'P')
would evaluate to 0.5

fraction_of_day(11, 59, 59, 'P')
would evaluate to 0.999988426

Hints: Convert the time into seconds since midnight. You should also
handle the 12:00AM case specially.

Write a main function that produces the following neatly formatted table
using f- strings for formatted printing. You solution must use looping
to print the table. You will get no credit for a solution that uses,
say, 24 variables and/or 24 print statements instead of a loop.

Time            Fraction Since Midnight
12:00 AM        0.0000
 1:00 AM        0.0417
 2:00 AM        0.0833
 3:00 AM        0.1250
 4:00 AM        0.1667
 5:00 AM        0.2083
 6:00 AM        0.2500
 7:00 AM        0.2917
 8:00 AM        0.3333
 9:00 AM        0.3750
10:00 AM        0.4167
11:00 AM        0.4583
12:00 PM        0.5000
 1:00 PM        0.5417
 2:00 PM        0.5833
 3:00 PM        0.6250
 4:00 PM        0.6667
 5:00 PM        0.7083
... (Your solution should continue to 11pm)
"""


# Add a main function that prints out a formated table with
# f-strings, as described in the problem set.
def main():
    """Print out a formatted table of the hours of the day with their
    corresponding fractions of a day.
    """

    print()
    print(" Time           Fraction Since Midnight")

    for hour in range(24):

        if hour < 12:
            ampm = "A"
        else:
            ampm = "P"

        # Convert the "0th hour" to be "12".
        if hour == 0 or hour == 12:
            print_hour = 12
        else:
            print_hour = hour % 12

        print(f"{print_hour:>2}:00 {ampm}M        "
              f"{fraction_of_day(print_hour, 0, 0, ampm):.4f}")
    print()

def fraction_of_day(hour: int, min: int, sec: int, ampm: str) -> float:
    """Return the fraction of a day elapsed since midnight."""

    # Constant for number of seconds in a day.
    DAILY_SECS = 86400

    # Convert 12 to mean 0 hours.
    if hour == 12:
        hour = 0

    # Convert hours/minutes to seconds.
    hour_to_sec = hour * 3600
    min_to_sec = min * 60

    # If PM, add half the day's seconds.
    pm_sec = 0
    if ampm == "P":
        pm_sec = 43200

    secs_elapsed = hour_to_sec + min_to_sec + sec + pm_sec

    fraction = secs_elapsed / DAILY_SECS

    return fraction



# Run the main function if script is run directly.
if __name__ == "__main__":
    main()
