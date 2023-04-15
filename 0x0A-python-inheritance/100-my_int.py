#!/usr/bin/python3



"""This module defines a class MyInt that inherits from int
and inverts the == and != operators."""


class MyInt(int):
    """A class that inherits from int and inverts the == and != operators."""


    def __eq__(self, value):
        """Override the == operator with the behavior of !=."""
        return self.real != value

    def __ne__(self, value):
        """Override the != operator with the behavior of ==."""
        return self.real == value
