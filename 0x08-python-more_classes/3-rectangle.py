#!/usr/bin/python3
class Rectangle:
   """Represent a triangle."""


def __init__(self, width=0, height=0):
    """Initialize a new Rectangle.

    Args:
        width (int): The width of a new rectangle.
        height (int): The height of the new rectangle.
    """

    self.width = width
    self.height = height

@property
def width(self):
    """Get/set the width of the Rectangle."""
    return self.width

@width.setter
def width(self, value):
    if not isinstance(value, int):
        raise TypeError("width must be an integer")
    if value < 0:
        raise ValueError("width must be >= 0")
    self._width = value

@property
def height(self):
    """Get/set the height of the Rectangle."""
    return self._height

@height.setter
def height(self, value):
    if not isinstance(value, int):
        raise TypeError("height must be an integer")
    if value < 0:
        raise ValueError("height must be >= 0")
    self._height = value


def area(self):
   """Return the area of the Rectangle."""
   return self._width * self._height

def perimeter(self):
    """Return the Parameter of the Rectangle."""
    return 2 * (self._width + self._height)

def __str__(self):
    """Return the printable representation of the Rectangle.

    Represents the rectangle with the # character.
    """

    if self._width == 0 or self._height == 0:
        return "\n".join(["#" * self._width for i in range(self._height)])
