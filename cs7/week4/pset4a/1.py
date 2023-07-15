"""
1.  s.count("o")
2.  s.count('stuck')
3.  s.find('Friend')
4.  s.find('enemy', 4)
5.  s[2].islower()
6.  s[0:5] == 'Your'
7.  s[0:5].upper()
"""


def main():
    """Test the questions."""

    s = "Your Friend Is Stuck. You Give Me Money, I Make Him Unstuck."

    print("'", end="")
    question = s[0:5].upper()
    print(question, end="")
    print("'")

if __name__ == "__main__":
    main()