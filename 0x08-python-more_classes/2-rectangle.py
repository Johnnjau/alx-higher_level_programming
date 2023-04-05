#!/usr/bin/python3
"""Represent a rectangle."""


class Rectangle:
    """Illustrates a rectangle"""

def __init__(self, width=0, height=0):
    """Initialize a new Rectangle.


    Args:
        width (int): The width of the new rectangle.
        height (int): The height of the new rectangle.
    """

    self._w = width
    self._h = height

@property
def height(self):
    """Get the height of the Rectangle."""
    return self._h

@height.setter
def height(self, value):
    if not isinstance(value, int):
        raise TypeError("height must be an integer")
    if value < 0:
        raise ValueError("height must be >= 0")
    self._h = value

@property
def width(self):
    """Get the width of the Rectangle."""
    return self._w

@width.setter
def width(self, value):
    if not isinstance(value, int):
        raise TypeError("width must be an integer")
    if value < 0:
        raise ValueError("width must be >= 0")
    self._w = value

def area(self):
    """Return the area of the Rectangle."""
    return self._h * self._w

def perimeter(self):
    """Return the perimeter of the Rectangle."""
    return (self._w + self._h) * 2 if self._w != 0 and self.h != 0 else 0
