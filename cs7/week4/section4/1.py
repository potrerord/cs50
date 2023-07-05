"""
a.	*Write an if statement that indicates the latest you’ll study (e.g. If before 10, print “Let’s keep going”, if after 10 print “It’s too late)
b.	*Make an if else statement about ‘finding a place to live’ or your ‘dream job requirements’ *Try to use a “and” student in your if statement – looking at three factors
c. Write a function that takes two numbers, a and b, and prints("Factor!") if a is a factor of b, and "Not a factor" if it is not.
(e.g.   6 is divisible by 2, so it would print factor)
"""

def main():
    keep_studying(18)
    dream_job("not chill", "short", "short")
    def isfactor(17, 100000001)


# a) Write an if statement that indicates the latest you’ll study (e.g.
# If before 10, print “Let’s keep going”, if after 10 print “It’s too
# late")

def keep_studying(current_hr):
    latest = 22
    earliest = 6

    print("It is currently hour " + current_hr + "of the day.")

    if (current_hr % 24 < latest) and (current_hr % 24 > earliest):
        print("Let's keep going!")
    else:
        print("It's too late.")


# b) Make an if-else statement about ‘finding a place to live’ or your
# ‘dream job requirements’. Try to use an “and” statement in your if
# statement – looking at three factors.



def dream_job(manager, commute, workday):
    print("The manager is", manager)
    print("The commute is", commute)
    print("The workday is", workday)
    print()

    if (manager == "chill" and (commute == "short" or workday == "short")):
        print("Take the job.")
    else:
        print("Get out.")

# c) Write a function that takes two numbers, a and b, and
# prints("Factor!") if a is a factor of b, and "Not a factor" if it is
# not. (e.g.   6 is divisible by 2, so it would print factor)

def isfactor(a: int, b: int) -> bool:
    if b % a == 0:
        print("Factor!")
        return True
    else:
        print("Not a factor.")
        return False


main()