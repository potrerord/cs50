"""
a.	*Write an if statement that indicates the latest you’ll study (e.g. If before 10, print “Let’s keep going”, if after 10 print “It’s too late)
b.	*Make an if else statement about ‘finding a place to live’ or your ‘dream job requirements’ *Try to use a “and” student in your if statement – looking at three factors
c. Write a function that takes two numbers, a and b, and prints("Factor!") if a is a factor of b, and "Not a factor" if it is not.
(e.g.   6 is divisible by 2, so it would print factor)
"""

def main():



# a) Write an if statement that indicates the latest you’ll study (e.g.
# If before 10, print “Let’s keep going”, if after 10 print “It’s too
# late")

def study_limit():
    if hour_of_day < 22:
        print("Let's keep going!")
    else:
        print("It's too late.")


# b) Make an if-else statement about ‘finding a place to live’ or your
# ‘dream job requirements’. Try to use an “and” statement in your if
# statement – looking at three factors.

def dream_job():
    if (manager == chill and (commute == short or workday == short)):
        accept()
    else:
        reject()

# c) Write a function that takes two numbers, a and b, and
# prints("Factor!") if a is a factor of b, and "Not a factor" if it is
# not. (e.g.   6 is divisible by 2, so it would print factor)

def is_factor(a: int, b: int) -> bool:
    if b % a == 0:
        print("Factor!")
        return True
    else:
        print("Not a factor.")
        return False


main()