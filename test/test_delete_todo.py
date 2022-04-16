import unittest
import json
from modules import todo_processor


class TestDeleteTodo(unittest.TestCase):
    """
    It tests the delete_todo function of the todo_processor module.
    """
    def setUp(self):
        """
        It initializes the .json file with 3 to do items.
        :return: none
        """
        with open("data.json", "w") as file:
            test_list = [{"id": 0, "title": "test1", "timestamp": 1650105904, "done": False},
                         {"id": 1, "title": "test2", "timestamp": 1650105905, "done": False},
                         {"id": 2, "title": "test3", "timestamp": 1650105906, "done": False}]
            json.dump(test_list, file)

    def test_delete_todo(self):
        """
        It tests the behaviour of the code when a to do list item is deleted.
        :return: none
        """
        with open("data.json", "r") as file:
            todo_processor.delete_todo(2)
            todo_list = json.load(file)
            self.assertTrue(todo_list)
            self.assertEqual(2, len(todo_list))

    def test_delete_all_todos(self):
        """
        It tests the behaviour of the code when all the items are deleted.
        :return: none
        """
        with open("data.json", "r") as file:
            todo_processor.delete_todo(0)
            todo_processor.delete_todo(1)
            todo_processor.delete_todo(2)
            todo_list = json.load(file)
            self.assertFalse(todo_list)
            self.assertEqual(0, len(todo_list))
