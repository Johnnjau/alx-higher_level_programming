#!/usr/bin/python3
"""This module defines a Rectangle class that inherits from BaseGeometry."""


from typing import Union
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that represents a rectangle using BaseGeometry."""


    def __init__(self, width: int, height: int) -> None:
        """ Initializes a new instance of the Rectangle class.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle."""
        super().__init__()
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
    def integer_validator(self, name: str, value: int) -> None:
        """ Validates the value of an integer.

        Args:
            name (str): The name of the integer.
            value (int): The value to be validated.
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0."""
      
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be > 0")
        return value
