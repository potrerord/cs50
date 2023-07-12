


def main():
    print()
    a()
    print()


"""
a.  Write a program that asks for the user to enter in a number between
    1-9, and if they enter a number out of that range, asks them to
    re-enter the number (using a while loop).
"""


def a():
    LOW = 1
    HIGH = 9

    while True:
        try:
            user_int = int(input(f"Enter a number between {LOW} and {HIGH}: "))
            if user_int < LOW or user_int > HIGH:
                raise ValueError
        except ValueError:
            print(f"error: number must be int between {LOW} and {HIGH}\n")
        else:
            return


"""
b.  Write a program that asks a user to enter a password, until their
    answer matches the password “DouDou”
"""


def b():
    PASSWORD = DouDou

    user_password = input("Enter password: ")

    while user_password != PASSWORD:
        user_password = input("Enter password: ")


"""
c.  You've decided not to drink coffee for 10 days straight, write a
    program (using a while loop) that asks the user to enter whether or
    not they drank coffee each day for 30 days, and then uses a Boolean
    value (True if you succeeded, False if you broke and drank coffee
    within the range) to state whether or not the user was successful.
"""


def c():



if __name__ == "__main__":
    main()
