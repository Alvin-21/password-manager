import unittest
from user_credentials import User, Credentials

class TestUser(unittest.TestCase):

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

    def setUp(self):
        """
        Set up method to run before each test case.
        """

        self.new_user = User("John", "Doe", "jdoe", "jaribu1")

    def test_init(self):
        """
        Test if the object is initialized properly.
        """

        self.assertEqual(self.new_user.fname, "John")
        self.assertEqual(self.new_user.lname, "Doe")
        self.assertEqual(self.new_user.username, "jdoe")
        self.assertEqual(self.new_user.password, "jaribu1")

    def test_save_user(self):
        """
        Test if the user object is saved into the user list.
        """

        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

if __name__ == '__main__':
    unittest.main()