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
