"""
This module contains functions to validate the user input.
"""


def validate_title_length(title):
    """
    This function checks if the title length is at least 5 characters.
    :param title: the title
    :return: True if length >= 5 otherwise False
    """
    if len(title) >= 5:
        return True
    return False
