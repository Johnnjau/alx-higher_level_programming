#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL.

Usage: ./1-hbtn_header.py <URL>
"""
import sys
import urllib.request


if __name__ == "__main__":
    import urllib.request as request
    from sys import argv
    req = request.Request(argv[1])
    with request.urlopen(req) as response:
        print(response.headers.get('X-Request-Id'))
