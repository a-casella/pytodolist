import unittest
import json
from modules import todo_processor


class TestChangeState(unittest.TestCase):
    """
    It tests the change_state function of the todo_processor module.
    """
    def setUp(self):
        """
        It initializes the .json file with 3 to do items with different states.
        :return: none
        """
        with open("data.json", "w") as file:
            test_list = [{"id": 0, "title": "test1", "timestamp": 1650105904, "done": False},
                         {"id": 1, "title": "test2", "timestamp": 1650105905, "done": True},
                         {"id": 2, "title": "test3", "timestamp": 1650105906, "done": False}]
            json.dump(test_list, file)

    def test_change_state(self):
        """
        It tests the behavior of the code in case of multiple state changes.
        :return: none
        """
        with open("data.json", "r") as file:
            todo_list = json.load(file)
            self.assertTrue(todo_list)
            self.assertEqual(len(todo_list), 3)
            self.assertEqual(int(todo_list[0]["done"]), False)
            todo_processor.change_state(0)
            self.assertEqual(int(todo_list[1]["done"]), True)
            todo_processor.change_state(1)
            self.assertEqual(int(todo_list[2]["done"]), False)
            todo_processor.change_state(2)
            file.seek(0)
            todo_list = json.load(file)
            self.assertEqual(int(todo_list[0]["done"]), True)
            self.assertEqual(int(todo_list[1]["done"]), False)
            self.assertEqual(int(todo_list[2]["done"]), True)
