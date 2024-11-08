#!/usr/bin/python3
"""list of available attributes and methods of an object"""


def lookup(obj):
''' return list attribute '''

    return list(dir(obj))
