#!/usr/bin/python3
"""Defines a file-writing function."""


def write_file(filename="", text=""):
    """
    Write a string to a UTF8 text file.


    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.

    Returns:
        The number of characters written.

    Raises:
        TypeError: If either filename or a text is not a string.
        IOError: If there is an error while writing to the file.
    """

if not isinstance(filename, str):
    raise TypeError("filename must be a string")
if not isinstance(text, str):
    raise TypeError("text must be a string")

try:
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
    except IOError as e:
        raise IOError(f"Error writing to {filename}: {e}")
