#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):


    """Print the first nb_lines lines of a UTF8 text file."""


    with open(filename, 'r', encoding='utf-8') as f:
        if nb_lines <= 0:
            print(f.read(), end='')
            return
        for i, line in enumerate(f):
            if i == nb_lines:
                break
            print(line, end='')
