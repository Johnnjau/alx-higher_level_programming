#!/usr/bin/python3
from 3-is_kind_of_class.py import is_instance_or_inherited

a = 1
if is_instance_or_inherited(a, int):
    print("{} comes from {}".format(a, int.__name__))
if is_kind_of_class(a, float):
    print("{} comes from {}".format(a, float.__name__))
if is_kind_of_class(a, object):
    print("{} comes from {}".format(a, object.__name__))
