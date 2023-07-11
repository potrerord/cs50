"""Takes two command line arguments and prints their sum."""


import sys


def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python addition.py x y")


# Run main function if script is run directly.
if __name__ == "__main__":
    main()
