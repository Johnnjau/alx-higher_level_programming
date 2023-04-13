#!/usr/bin/python3
# 4-inherits_from.py


"""Defines a function to check if an object is an instance of a
specific class or its  subclass."""


def inherits_from(obj, a_class):
    """This function checks if an object is an instance of a subclass
    of the given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.

    Returns:
        bool: True if obj is an instance of a subclass of a_class, False otherwise.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else;
        return False
