#!/usr/bin/python3
"""convert file object to json """


import json


def save_to_json_file(my_obj, filename):
    """return object with json"""
    with open(filename, "w+") as f:
        return json.dump(my_obj, f)
