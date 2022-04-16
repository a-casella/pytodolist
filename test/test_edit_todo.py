import unittest
import json
from modules import todo_processor


class TestEditTodo(unittest.TestCase):
    """
    It tests the edit_todo function of the todo_processor module.
    """
    def setUp(self):
        """
        It initializes the .json file with 3 to do items.
        :return: none
        """
        with open("data.json", "w") as file:
            test_list = [{"id": 0, "title": "test", "timestamp": 1650105904, "done": False},
                         {"id": 1, "title": "abcd", "timestamp": 1650105905, "done": True},
                         {"id": 2, "title": "title", "timestamp": 1650105906, "done": False}]
            json.dump(test_list, file)

    def test_edit_todo(self):
        """
        It tests the behavior of the code in case of multiple state changes.
        :return: none
        """
        with open("data.json", "r") as file:
            todo_list = json.load(file)
            self.assertTrue(todo_list)
            self.assertEqual(len(todo_list), 3)
            self.assertEqual(todo_list[0]["title"], "test")
            todo_processor.edit_todo(0, "edited_test")
            self.assertEqual(todo_list[1]["title"], "abcd")
            todo_processor.edit_todo(1, "edited_abcd")
            self.assertEqual(todo_list[2]["title"], "title")
            todo_processor.edit_todo(2, "edited_title")
            file.seek(0)
            todo_list = json.load(file)
            self.assertEqual(todo_list[0]["title"], "edited_test")
            self.assertEqual(todo_list[1]["title"], "edited_abcd")
            self.assertEqual(todo_list[2]["title"], "edited_title")
