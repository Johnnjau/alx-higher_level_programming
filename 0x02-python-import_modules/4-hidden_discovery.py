#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    from hidden_4.pyc import name

    names = dir(hidden_4.pyc)
    for names in names:
        if name[:2] != "__":
            print(name)
