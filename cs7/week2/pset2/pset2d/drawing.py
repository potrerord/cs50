"""
Recreates drawing specified in #16 of Pset2 Part D.
"""


def main():
    """Call other drawing functions with print() newlines."""
    
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
    """Draw top half of hexagon."""

    print("  _______")
    print(" /       \\")
    print("/         \\")


def bottom():
    """Draw bottom half of hexagon."""

    print("\\         /")
    print(" \\_______/")


def chain():
    """Draw chain."""

    print("-\"-'-\"-'-\"-")

def hexagon():
    """Draw full hexagon by combining top() and bottom()."""

    top()
    bottom()


main()
