#!/usr/bin/python3
import unitest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
"""A class containing the test cases"""


class TestBase(unittest.TestCase):
    def test_id(self):
        b1 = Base()
        b2
