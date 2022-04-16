"""
This module contains functions used to store, read and initialize data from a .json file.
"""

import os.path
import json


def init_data_file():
    """
    It creates and initializes the .json file if it doesn't exist.
    :return: none
    """
    if not(os.path.exists("data.json")):
        with open("data.json", "w") as file:
            json.dump([], file)


def read_list():
    """
    It reads the stored data.
    :return: a list of to do items
    """
    with open("data.json", "r") as file:
        return json.load(file)


def write_list(todos):
    """
    It saves the list of to do items.
    :param todos: a list to do items
    :return: none
    """
    with open("data.json", "w") as file:
        json.dump(todos, file)
