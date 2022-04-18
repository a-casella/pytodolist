import unittest
from modules import input_validator


class TestInputValidator(unittest.TestCase):
    """
    It tests the input_validator module functions.
    """

    def test_validate_title_length(self):
        """
        It tests the behavior of the validate_title_length to check if it validates correctly
        the title inserted by the user.
        :return: none
        """
        self.assertFalse(input_validator.validate_title_length("abcd"))
        self.assertTrue(input_validator.validate_title_length("abcde"))
        self.assertTrue(input_validator.validate_title_length("abcde1"))


