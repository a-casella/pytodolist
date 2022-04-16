import unittest
import json
from modules import todo_processor


class TestAddTodo(unittest.TestCase):
    """
    It tests the add_todo function of the todo_processor module.
    """
    def setUp(self):
        """
        It initializes the .json file.
        :return: none
        """
        with open("data.json", "w") as file:
            json.dump([], file)

    def test_add_todo_empty_list(self):
        """
        It tests the behavior in case of an empty list.
        :return: none
        """
        todo_processor.add_todo("test")
        with open("data.json", "r") as file:
            todo_list = json.load(file)
            self.assertTrue(todo_list)
            self.assertEqual(len(todo_list), 1)
            self.assertEqual(int(todo_list[0]["id"]), 0)
            self.assertEqual(todo_list[0]["title"], "test")

    def test_add_todo_incremental_items(self):
        """
        It tests the behavior in case of multiple adds.
        :return: none
        """
        todo_processor.add_todo("test1")
        todo_processor.add_todo("test2")
        todo_processor.add_todo("test3")
        with open("data.json", "r") as file:
            todo_list = json.load(file)
            self.assertTrue(todo_list)
            self.assertEqual(len(todo_list), 3)
            self.assertEqual(int(todo_list[0]["id"]), 0)
            self.assertEqual(todo_list[2]["title"], "test3")
