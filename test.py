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

    def user_set_up(self):
        """
        Set up method to run before each test case.
        """

        self.new_user = User("John", "Doe", "jdoe", "jaribu1")

    def test_init(self):
        '''
        Test if the object is initialized properly.
        '''

        self.assertEqual(self.new_user.fname, "John")
        self.assertEqual(self.new_user.lname, "Doe")
        self.assertEqual(self.new_user.username, "jdoe")
        self.assertEqual(self.new_user.password, "jaribu1")