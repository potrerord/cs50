"""
The following requirement for membership in the Congress of the United
States are quoted from Article I of the Constitution of the United
States:

a)  No Person shall be a Representative who shall not have attained to
    the Age of twenty-five Years, and been seven Years a Citizen of the
    United States, and who shall not, when elected, be an Inhabitant of
    that State in which he shall be chosen.
b)  No Person shall be a senator who shall not have attained to the Age
    of thirty Years, and been nine Years a Citizen of the United States,
    and who shall not, when elected, be an Inhabitant of that State for
    which he shall be chosen.

Write a function named eligible_for_senate that returns a boolean value,
and another function named eligible_for_house that also returns a
boolean value. Both functions accept two integer arguments (via
parameters named age and length_of_citizenship), and each returns the
corresponding congressional eligibility as a boolean value.

You should show that these examples work with your functions by making
the appropriate function calls in main:

a)  Someone of age 37 and 3 years of citizenship is not eligible for
    election to either the House or the Senate, so the functions should
    both return False.
    
b)  Someone of age 47 and 8 years of citizenship is eligible for
    election to the House but not the Senate, so
    eligible_for_house(47, 8) should return True, but
    eligible_for_senate(47, 8) should return False.
"""


# Implement eligible_for_sentate here.
#
# Returns true if the candidate is eligibe to run for senate.
# Does not print anything out.
def eligible_for_sentate(*** replace with your parameters ***):
    *** add your code here ***


# Implement eligible_for_house here.
#
# Returns true if the candidate is eligible for the house.
# Does not print anything out.
def eligible_for_house(*** replace with your parameters ***):
    *** add your code here ***


# Add a main that tests out your functions as specified in the problem.
def main():
    *** add your test cases here ***

# Runs the main function. Leave as is.
if __name__ == "__main__":
    main()
