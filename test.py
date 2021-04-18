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
        self.new_credential = Credentials("Instagram", "doej", "trial2")

    def test_user_init(self):
        """
        Test if user object is initialised properly.
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

    def test_save_multiple_users(self):
        """
        Check if we can save multiple user objects to our user_list.
        """

        self.new_user.save_user()
        test_user = User("Test", "User", "tuser", "testing20")
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)

    def test_user_exists(self):
        """
        Test to check if we can return a Boolean if we cannot find the user.
        """

        self.new_user.save_user()
        test_user = User("Test", "User", "tuser", "testing20")
        test_user.save_user()
        user_exists = User.user_exist("tuser")
        self.assertTrue(user_exists)

    def test_verify_user(self):
        """
        Test to check if we can return a Boolean if the user login deatils don't match.
        """

        self.new_user.save_user()
        test_user = User("Test", "User", "tuser", "testing20")
        test_user.save_user()
        user_verification = User.verify_user("tuser", "testing20")
        self.assertTrue(user_verification)

    def test_credential_init(self):
        """
        Test if credential object is initialised properly.
        """

        self.assertEqual(self.new_credential.app, "Instagram")
        self.assertEqual(self.new_credential.username, "doej")
        self.assertEqual(self.new_credential.password, "trial2")


if __name__ == '__main__':
    unittest.main()