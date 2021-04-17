from random import choice

class User:
    """
    Class that generates new instances of users.
    """

    user_list = []

    def __init__(self, fname, lname, username, password):
        self.fname = fname
        self.lname = lname
        self.username = username
        self.password = password

    def save_user(self):
        """
        saves user objects into user_list
        """

        User.user_list.append(self)

    @classmethod
    def user_exist(cls, username):
        """
        Method that checks if a user exists from the user list.
        Args:
            username: username to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        """
        for user in cls.user_list:
            if user.username == username:
                return True

        return False

class Credentials:
    """
    Class that generates new credential instances.
    """

    credential_list = []

    def __init__(self, app, username, password):
        self.app = app
        self.username =username
        self.password = password

    def save_credentials(self):
        """
        Saves newly created credential objects into credential_list.
        """

        Credentials.credential_list.append(self)

    def delete_credential(self):
        """
        Deletes a saved credential account from the credential_list.
        """

        Credentials.credential_list.remove(self)

    @classmethod
    def password(cls, len=8, chars=string.letters+string.digits):
        """
        Auto-generates a password for the user.
        """

        return ''.join([choice(chars) for i in range(len)])

    @classmethod
    def display_credentials(cls):
        """
        Reuturns the credential list.
        """

        return cls.credential_list

    @classmethod
    def display_app_credential(cls, app):
        """
        Returns the specified app credential.
        """

        for credential in cls.credential_list:
            if credential.app == app:
                return credential