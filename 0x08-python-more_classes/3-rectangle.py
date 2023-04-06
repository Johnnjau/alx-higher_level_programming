#!/usr/bin/python3
"""Rectangle class with width and height attributes"""


class Rectangle:
    def __init__(self, w=0, h=0):
        self.w = w
        self.h = h

@property
def w(self):
    return self._w

@w.setter
def w(self, value):
    if not isinstance(value, int):
        raise TypeError("width must be an integer")
    if value < 0:
        raise ValueError("width must be >= 0")
    self.__w = value

@property
def h(self):
    return self._h

@h.setter
def h(self, value):
    if not isinstance(value, int):
        raise TypeError("height must be an integer")
    if value < 0:
        raise ValueError("height must be >= 0")
    self.__h = value

def area(self):
    return (self.__w * self.__h)

def perimeter(self):
    if self.__w == 0 or self.__h == 0:
        return 0
    return ((self.__w * 2) + (self.__h * 2))

def __str__(self):
    if self.__w == 0 or self.__h == 0:
        return""
    return ("\n".join(['#' * self.__w for i in range(self.__h)]))
