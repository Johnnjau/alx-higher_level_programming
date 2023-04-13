#!/usr/bin/python3

"""Defines an object attribute lookup function"""


def lookup(obj_to_inspect):
    """Return a list of an object's attributes."""
    return dir(obj_to_inspect)
