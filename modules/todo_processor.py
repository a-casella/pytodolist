"""
This module contains functions used to carry out data processing required by the functionalities of the application.
"""
import time
from modules import file_handler
from classes.Todo import Todo
from operator import itemgetter


def add_todo(title):
    """
    It adds a new to do item.
    :param title: title of the to do item
    :return: none
    """
    todo_list = file_handler.read_list()
    id_todo = 0
    # if the list is not empty
    if todo_list:
        id_todo = max(todo["id"] for todo in todo_list) + 1
    todo = Todo(id_todo, title, round(time.time()), False)
    todo_list.append(todo.__dict__)
    file_handler.write_list(todo_list)


def list_desc():
    """
    It returns the list of to do items in descending order.
    :return: the list of to do items
    """
    todo_list = file_handler.read_list()
    # key gets a function callable to be applied to the todos list
    todo_list.sort(key=itemgetter("id"), reverse=True)
    return todo_list


def delete_todo(id_todo):
    """
    It deletes a selected to do item by its id.
    :param id_todo: the id of the to do item
    :return: none
    """
    todo_list = file_handler.read_list()
    # list comprehension where the result is a new list without the item with id equal to the one
    # inserted by the user
    new_todo_list = [todo for todo in todo_list if not todo["id"] == id_todo]
    file_handler.write_list(new_todo_list)


def change_state(id_todo):
    """
    It changes(toggles) the state of a selected to do item from False to True and vice versa using its id.
    :param id_todo: the id of the to do item
    :return: none
    """
    todo_list = file_handler.read_list()
    for todo in todo_list:
        if todo["id"] == id_todo:
            todo["done"] = not todo["done"]
            break
    file_handler.write_list(todo_list)
