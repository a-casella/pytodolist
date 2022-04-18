"""
This module contains functions used to carry out data processing required by the functionalities of the application.
"""
import time

from classes.TodoSchema import TodoSchema
from modules import file_handler
from classes.Todo import Todo


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
        id_todo = max(todo.id for todo in todo_list) + 1
    todo = Todo(id_todo, title, round(time.time()), False)
    todo_list.append(todo)
    file_handler.write_list(todo_list)


def list_desc():
    """
    It returns the list of to do items in descending order.
    :return: the list of to do items
    """
    todo_list = file_handler.read_list()
    # key gets an anonymous function to get the timestamp of the item
    todo_list.sort(key=lambda item: item.timestamp, reverse=True)
    schema = TodoSchema(many=True)
    return schema.dump(todo_list)


def delete_todo(id_todo):
    """
    It deletes a selected to do item by its id.
    :param id_todo: the id of the to do item
    :return: none
    """
    todo_list = file_handler.read_list()
    # list comprehension where the result is a new list without the item with id equal to the one
    # inserted by the user
    new_todo_list = [todo for todo in todo_list if not todo.id == id_todo]
    file_handler.write_list(new_todo_list)


def change_state(id_todo):
    """
    It changes(toggles) the state of a selected to do item from False to True and vice versa by using its id.
    :param id_todo: the id of the to do item
    :return: none
    """
    todo_list = file_handler.read_list()
    for todo in todo_list:
        if todo.id == id_todo:
            todo.done = not todo.done
            break
    file_handler.write_list(todo_list)


def edit_todo(id_todo, title):
    """
    It edits the title of a to do item by using its id and the new title.
    :param id_todo: the id of the to do item
    :param title: the new title
    :return: none
    """
    todo_list = file_handler.read_list()
    for todo in todo_list:
        if todo.id == id_todo:
            todo.title = title
            break
    file_handler.write_list(todo_list)


def search_todo(title):
    """
    It searches for a selected to do item by using its title.
    :param title: the title of the to do item
    :return: none
    """
    result_list = []
    todo_list = file_handler.read_list()
    for todo in todo_list:
        if title in todo.title:
            result_list.append(todo)
    schema = TodoSchema(many=True)
    return schema.dump(result_list)
