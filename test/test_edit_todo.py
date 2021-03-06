import unittest
import json

from classes.TodoSchema import TodoSchema
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
            schema = TodoSchema(many=True)
            todo_list = schema.load(json.load(file))
            self.assertTrue(todo_list)
            self.assertEqual(3, len(todo_list))
            self.assertEqual("test", todo_list[0].title)
            todo_processor.edit_todo(0, "edited_test")
            self.assertEqual("abcd", todo_list[1].title)
            todo_processor.edit_todo(1, "edited_abcd")
            self.assertEqual("title", todo_list[2].title)
            todo_processor.edit_todo(2, "edited_title")
            file.seek(0)
            todo_list = schema.load(json.load(file))
            self.assertEqual("edited_test", todo_list[0].title)
            self.assertEqual("edited_abcd", todo_list[1].title)
            self.assertEqual("edited_title", todo_list[2].title)
