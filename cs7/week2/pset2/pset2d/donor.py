"""
Classifies charity contributors as Benefactors, Patrons, Suppporters,
Friends, or Cheapskates based on different donation tiers.
"""


def main():
    """Print result of donor function."""

    print(donor() + "!\n")


def donor() -> str:
    """Return donor designation based on size of user-input donation."""

    # Define lower-limit thresholds for each donation tier.
    benefactor_floor = 10000
    patron_floor = 1000
    supporter_floor = 200
    friend_floor = 15

    # Get donation from user. Print error if negative input.
    donation = float(input("\nEnter the amount of a contribution: "))
    if donation < 0:
        return "error: contribution must be nonnegative"

    # Return appropriate string for donation amount.
    if donation >= benefactor_floor:
        return "Benefactor"
    elif donation >= patron_floor:
        return "Patron"
    elif donation >= supporter_floor:
        return "Supporter"
    elif donation >= friend_floor:
        return "Friend"
    else:
        return "Cheapskate"


main()