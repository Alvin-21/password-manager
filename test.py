import unittest
from user_credentials import User, Credentials

class TestContact(unittest.TestCase):

    """
    Test class that defines test cases for the user and credential class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """

    def tearDown(self):
        """
        Cleans up after each test case has run.
        """
        User.user_list = []
        Credentials.credential_list = []