#!/usr/bin/python3
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
"""Define a class containing the test cases"""


class TestBase(unittest.TestCase):
    """Test for the id attribute"""
    def test_id(self):
        base1 = Base()
        base2 = Base(98)
        base3 = Base()
        base4 = Base(1)
        base5 = Base(0)
        base6 = Base(-3)

        """Assert that the to_json_string method returns the expected values"""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(type(Base.to_json_string([{}])), str)
        self.assertEqual(Base.to_json_string([{}]), "[{}]")
        self.assertEqual(
            type(Base.to_json_string([
                base1.to_dictionary(),
                base2.to_dictionary()
            ])),
            str)
        self.assertEqual(
            Base.to_json_string([base1.to_dictionary(), base2.to_dictionary()]),
            '[{"id": 1}, {"id": 98}]')
    
    """Test for the save_to_file method"""
    def test_save_to_file(self):
        base1 = Base()
        base2 = Base(98)

    """Assert that the to_json_string method returns the expected values"""
    self.assertEqual(Base.to_string(None), "[]")
    self.assertEqual(Base.to_string([]), "[]")
    self.assertEqual(type(Base.to_string([{}])), str)
    self.assertEqual(Base.to_json_string([{}]), "[{}]")
    self.assertEqual(
        type(Base.to_json_string([
            base1.to_dictionary(),
            base2.to_dictionary()
        ])),
        str)
    self.assertEqual(
        Base.to_json_string([base1.to_dictionary(), base2.to_dictionary()]),
        '[{"id": 1}, {"id": 98}]')
    
    """Test for the save_to_file method"""
    def test_save_to_file(self):
        base1 = Base()
        base2 = Base(98)
        Base.save_to_file([base1, base2])

        with open("Base.json", "r") as file:
            """Assert that the saved data matches the expected values"""
            self.assertEqual(
                json.loads(file.read()), [
                    base1.to_dictionary(),
                    base2.to_dictionary()
                ])
    """Test for the load_from_file method"""
    def test_load_from_file(self):
        base1 = Base()
        base2 = Base(98)
        Base.save_to_file([base1, base2])

        """Load the saved data and assert that it matches the expected values"""
        obj = Base.load_from_file()
        self.assertEqual(len(obj), 2)
        self.assertIsInstance(obj[0], Base)
        self.assertIsInstance(obj[1], Base)
        self.assertEqual(obj[0].id, 1)
        self.assertEqual(obj[1].id, 98)


if __name__ == "__main__":
    unittest.main()

