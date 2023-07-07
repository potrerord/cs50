
test = "cat"



def main():
    print_chars(test)

    print(is_odd_len(test))
    print(fourth_char(test))
    print(truncate(test))


"""
1)  Write a function print_chars(s) that takes a string s and prints out
    each character of a given string, each on its own line.
"""

def print_chars(s: str) -> None:
    """Print every character in string argument."""

    for i in range(len(s)):
        print(s[i])


"""
2)  Write a function is_odd_len(s) that takes a string s and returns
    True if the number of characters in s is odd, and False if it is
    even.
"""

def is_odd_len(s: str):
    """Return bool indicating whether string argument has odd length."""

    # Return False if even.
    if len(s) % 2 == 0:
        return False

    # Return True if odd.
    return True


"""
3)  Write a function fourth_char(s) that takes a string s and returns
    the fourth letter of a given string, or None if the string has fewer
    than 4 letters.
"""

def fourth_char(s: str):
    """Return the fourth letter of string argument."""

    # Return None if the string has fewer than 4 letters.
    if len(s) < 4:
        return

    # Return the fourth character if it exists.
    return s[3]



"""
4)  Write a function truncate(s) that takes a string s. If the string is
    10 characters orless, then it returns the string unchanged. If the
    string is more than 10 characters, itreturns the first 10 characters
    of the string.

    Note: You may be tempted to use an if statement because of the
    wording of the problem. However, because of the way slicing works,
    it is possible to do this without any if!
"""

def truncate(s: str):
    """Return first 10 characters of string argument."""
    return s[:10]


# Run the main function if script is run directly.
if __name__ == "__main__":
    main()
