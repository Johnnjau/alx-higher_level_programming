#!/usr/bin/python3
"""This module defines the BaseGeometry Class."""


class BaseGeometry:
    """A class that represents base geometry."""
    def area(self):
        """Computes the area of the geometric shape.
        This method needs to be implemented in derived classes."""

        raise NotImplementedError("The 'area' method is  not implemented.")
