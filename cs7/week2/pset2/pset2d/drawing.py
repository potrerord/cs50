"""
Recreates drawing specified in #16 of Pset2 Part D.
"""


def main():
    hexagon()

    print()

    chain()
    hexagon()

    print()
    print()

    chain()
    bottom()

    print()
    
    top()
    chain()
    bottom()


def top():
    print("  _______")
    print(" /       \\")
    print("/         \\")


def bottom():
    print("\\         /")
    print(" \\_______/")


def chain():
    print("-\"-'-\"-'-\"-")

def hexagon():
    top()
    bottom()


main()
