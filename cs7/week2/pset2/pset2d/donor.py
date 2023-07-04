"""
Classifies charity contributors as Benefactors, Patrons, Suppporters,
Friends, or Cheapskates based on different donation tiers.
"""


def main():
    """Get user input"""

    user_donation = float(input("\nEnter the amount of a contribution: "))
    print(donor(user_donation) + "!\n")


def donor(donation: float) -> str:
    """Return donor designation based on size of donation.

    Keyword argument:
    donation -- Float value representing size of donation.
    """

    if donation >= 10000:
        return "Benefactor"
    elif donation >= 1000:
        return "Patron"
    elif donation >= 200:
        return "Supporter"
    elif donation >= 15:
        return "Friend"
    else:
        return "Cheapskate"


main()