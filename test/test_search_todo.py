import unittest
import json
from modules import todo_processor


class TestListDesc(unittest.TestCase):
    """
    It tests the search_todo function of the todo_processor module.
    """

    def setUp(self):
        """
        It initializes the .json file with 10 to do items.
        :return: none
        """
        with open("data.json", "w") as file:
            test_list = [{"id": 0, "title": "test1", "timestamp": 1650105904, "done": False},
                         {"id": 1, "title": "test2", "timestamp": 1650105905, "done": True},
                         {"id": 2, "title": "test3", "timestamp": 1650105906, "done": False},
                         {"id": 3, "title": "abcd", "timestamp":  1650105907, "done": False},
                         {"id": 4, "title": "test4", "timestamp": 1650105908, "done": True},
                         {"id": 5, "title": "test5", "timestamp": 1650105909, "done": False},
                         {"id": 6, "title": "test6", "timestamp": 1650105910, "done": False},
                         {"id": 7, "title": "abcd1", "timestamp": 1650105911, "done": True},
                         {"id": 8, "title": "test7", "timestamp": 1650105912, "done": False},
                         {"id": 9, "title": "abcd3", "timestamp": 1650105913, "done": False}]
            json.dump(test_list, file)

    def test_search_todo(self):
        """
        It tests the behavior of the code when the user searches for a to do item with a title
        :return: none
        """
        todo_list = todo_processor.search_todo("test")
        self.assertTrue(todo_list)
        self.assertEqual(7, len(todo_list))
        todo_list = todo_processor.search_todo("abcd")
        self.assertTrue(todo_list)
        self.assertEqual(3, len(todo_list))
        todo_list = todo_processor.search_todo("title")
        self.assertFalse(todo_list)
        self.assertEqual(0, len(todo_list))

