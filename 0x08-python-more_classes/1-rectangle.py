<<<<<<< HEAD
#!/usr/bin/python3
"""Definition of a class Rectangle"""


class Rectangle:
    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height
        self.check_dimensions()

    def check_dimensions(self):
        if not isinstance(self._width, int):
            raise TypeError("width must be an integer")
        if self._width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(self._height, int):
            raise TypeError("height must be an integer")
        if self._height < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value
        self.check_dimensions()

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
        self.check_dimensions()
=======
#!/usr/bin/python3
# 1-rectangle.py
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
>>>>>>> c99d2c489ff95f8b804e53d1fd225937d0ac6d47
