#!/usr/bin/python3
"""Rectangle class with width and height attributes"""


class Rectangle:
    """Defines a Rectangle object"""

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle object with width and height values"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width of the rectangle"""
        return self._width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle"""
        self._validate_input(value)
        self._width = value

    @property
    def height(self):
        """Gets the height of the rectagle"""
        return self._height

    @height.setter
    def height(self, value):
       """Sets the height of the rectangle"""
       self._validate_input(value)
       self._height = value

    def _validate_input(self, value):
        """Validates input for the width and height properties"""
        if not isinstance(value, int):
            raise TypeError("Value must be an integer")
        if value < 0:
            raise ValueError("Value must be >= 0")
