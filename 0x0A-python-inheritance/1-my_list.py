#!/usr/bin/python3

class MyList(list):
    """Implements sorted printing for the built-in list class"""

    def print_sorted(self):
        """Print the list in ascending order."""
        sorted_list = sorted(self)
        print(f"The sorted list is: {sorted_list}")
