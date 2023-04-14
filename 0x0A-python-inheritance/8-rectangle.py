#!/usr/bin/python3
# 8-rectangle.py
"""This module defines a Rectangle class that inherits from BaseGeometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that represents a rectangle using BaseGeometry."""


    def __init__(self, width, height):
        """ Initializes a new instance of the Rectangle class.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
    def __str__(self):
        """ Returns a string representation of the Rectangle object."""
        return f"[Rectangle] {self.__width}/{self.__height}"
    def area(self) -> Union[int, float]:
        """ Computes the area of a rectangle."""
        return self.__width * self.__height
    
    if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
    if value <= 0:
            raise ValueError(f"{name} must be > 0")
    return value
