"""Calculates using some formula."""

import math

def main():



def quad_formula_pos(a, b, c) -> float:
    """Solves a quadratic equation with constants a, b, and c, then
    returns the output if the solution exists. If the solution does not
    exist because the discriminant < 0, returns None.

    arguments:
    a -- leading coefficient (quadratic term)
    b -- middle coefficient (linear term)
    c -- constant term
    """

    discriminant = b ** 2 - 4 * a * c

    # If discriminant is <= 0, cut it
    if discriminant < 0:
        return None
    else:
        x = -b + math.sqrt(discriminant) / (2 * a)
        return x


main()