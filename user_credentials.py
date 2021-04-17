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

    @classmethod
    def password(cls, len=8, chars=string.letters+string.digits):
        return ''.join([choice(chars) for i in range(len)])