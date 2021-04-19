from user_credentials import User, Credentials

def create_user(fname, lname, username, password):
    """
    Creates a new user.
    """

    return User(fname, lname, username, password)

def create_credentials(app, username, password):
    """
    Creates new user credentials.
    """

    return Credentials(app, username, password)


def main():
    print("Hello, welcome to Password Manager")
    while True:
        print("Please use these short codes to execute your desired task: ca - create new account, li - login to account, ex - exit program")
        
        short_code = input().lower().strip()

        if short_code == "ca":
            fname = input("Enter your first name: ").strip()
            lname = input("Enter your last name: ").strip()
            username = input("Enter your preferred username: ").strip()
            password = input("Enter your password")

            new_user = create_user(fname, lname, username, password)
            new_user.save_user()
            
            print(f"Your new account has been created with the following details:\nName: {fname} {lname}\nUsername: {username}\nPassword: {password}")

if __name__ == '__main__':
    main()
