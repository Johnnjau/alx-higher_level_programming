#!/usr/bin/python3
#2-is_same_class.py


"""A function that checks if an object is an instance of a given class."""


def is_same_class(obj, a_class):

    """Function takes 2 arguments, an object and a class, and returns True if the 
    object is an instance of the class and false otherwise"""
    if type(obj) is a_class:
        return True
    else:
        return False
