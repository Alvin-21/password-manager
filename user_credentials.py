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