#!/usr/bin/python3

"""Defines an integer addition function."""


def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Float arguments are typecasted to ints before addition is performed.

    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    # Check if 'a' is an integer or float, else raise TypeError
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    # Check if 'b' is an integer or float, else raise TypeError
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Convert 'a' and 'b' to integers and return their sum
    return int(a) + int(b)
