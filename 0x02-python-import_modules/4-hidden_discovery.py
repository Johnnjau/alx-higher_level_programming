#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    from hidden_4 import hidden

    names = dir(hidden_4)
    for names in names:
        if name[:2] != "__":
            print(name)
