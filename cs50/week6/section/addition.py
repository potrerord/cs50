"""Takes two command line arguments and prints their sum."""


import sys


def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python addition.py x y")

    try:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    except ValueError:
        sys.exit("please enter two ints")
    else:
        xysum = x + y

    print(f"{x} + {y} = {xysum}")


# Run main function if script is run directly.
if __name__ == "__main__":
    main()
