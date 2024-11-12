#!/usr/bin/python3
""" fx open and adding  """


def append_write(filename="", text=""):
    """ adding text"""
    with open(filename, 'a+') as f:
        return f.write(text)
