#!/usr/bin/python3
""" use load method"""


import json


def load_from_json_file(filename):
    """use  load"""
    with open(filename, "r") as f:
        return json.load(f)
