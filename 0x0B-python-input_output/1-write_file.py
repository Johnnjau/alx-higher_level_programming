#!/usr/bin/python3
def number_of_lines(filename=""):
    """Return the number of lines in a text file."""
    with open(filename, 'r') as f:
        return sum(1 for _ in f)
