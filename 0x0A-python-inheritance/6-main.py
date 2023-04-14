#!/usr/bin/python3
BaseGeometry = __import__('6-base_geometry').BaseGeometry


bg = BaseGeometry()

try:
    print(bg.area())
    """Area is length multiplied by height"""
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
