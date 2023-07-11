"""
Prints the congressional eligibility of a person based on their age and
length of U.S. citizenship.
"""


def main():
    """Test functions."""

    #
    AGE1 = 37
    LENGTH1 = 3
    AGE2 = 47
    LENGTH2 = 8

    print()

    # Scenario A
    print("a)")
    print(eligible_for_house(AGE1, LENGTH1))
    print(eligible_for_senate(AGE1, LENGTH1))
    print()

    # Scenario B
    print("b)")
    print(eligible_for_house(AGE2, LENGTH2))
    print(eligible_for_senate(AGE2, LENGTH2))
    print()


def eligible_for_senate(age: int, length_of_citizenship: int) -> bool:
    """Return true if the candidate is eligible to run for senate."""

    # Return false if candidate is younger than 30.
    if age < 30:
        return False

    # Return False if candidate has not been a citizen for >= 9 years.
    if length_of_citizenship < 9:
        return False

    # Return True if neither are the case.
    return True


def eligible_for_house(age: int, length_of_citizenship: int) -> bool:
    """Returns true if the candidate is eligible for the house."""

    # Return false if candidate is younger than 25.
    if age < 25:
        return False

    # Return False if candidate has not been a citizen for >= 9 years.
    if length_of_citizenship < 7:
        return False

    # Return True if neither are the case.
    return True


# Run the main function if script is run directly.
if __name__ == "__main__":
    main()
