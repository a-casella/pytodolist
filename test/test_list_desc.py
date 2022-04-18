import unittest
import json
from modules import todo_processor


class TestListDesc(unittest.TestCase):
    """
    It tests the list_desc function of the todo_processor module.
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

    def test_list_desc(self):
        """
        It tests the behavior of the code when it is asked for a list of to do items in descending order.
        :return: none
        """
        todo_list = todo_processor.list_desc()
        self.assertTrue(todo_list)
        self.assertEqual(3, len(todo_list))
        self.assertEqual(2, int(todo_list[0]["id"]))
        self.assertEqual(1, int(todo_list[1]["id"]))
        self.assertEqual(0, int(todo_list[2]["id"]))
