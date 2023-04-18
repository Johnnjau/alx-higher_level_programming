#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_unique_id(self):
        b1 = Base()
        b2 = Base()
        self.assertNotEqual(b1.id, b2.id)
    
    def test_provided_id(self):
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_invalid_id(self):
        with self.assertRaises(TypeError):
            b = Base("invalid_id")

if __name__ == "__main__":
    unittest.main()