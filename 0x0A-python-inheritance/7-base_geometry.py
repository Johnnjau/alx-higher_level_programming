#!/usr/bin/python3
"""Defines a class BaseGeometry that provides common geometry methods."""


class BaseGeometry:
    """A base geometry class that provides common geometry methods."""


    def area(self):
        """Calculate the area of the geometry.
        Raises:
            Exception: If area method is not implemented."""
        raise Exception("area() is not implemented.")
    def integer_validator(self, name, value):
        """
        Validate the given value is an integer and greater than zero.

        Args:
            name (str): The name of the value.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to zero.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
