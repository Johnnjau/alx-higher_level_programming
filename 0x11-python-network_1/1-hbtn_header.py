#!/usr/bin/python3
"""
script takes in a URL, sends a request to the URL
"""
from urllib.request import urlopen
from sys import argv


if __name__ == "__main__":
    with urlopen(argv[1]) as response:
        header = response.getheader('X-Request-Id')
        print(header)
