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

            if User.user_exist(username):
                print("That username has already been taken. Please enter a different username.")
                username = input("Enter your preferred username: ").strip()
                
            password = input("Enter your password: ")

            new_user = create_user(fname, lname, username, password)
            new_user.save_user()
            
            print(f"Your new account has been created with the following details:\nName: {fname} {lname}\nUsername: {username}\nPassword: {password}")

        elif short_code == "li":
            print("Please enter your user details to login.")
            login_username = input("Enter your username: ").strip()
            login_password = input("Enter your password: ")

            user_verification = User.verify_user(login_username, login_password)

            if user_verification:
                print(f"Hello {login_username}, please use the following codes to select a task.")
                while True:
                    print("cc - Create Credentials\ndelc - Delete Credential\ndc -Display Credentials\ndsc - Display Specific Credential\nex - Exit")
                    code = input().lower().strip()

                    if code == "cc":
                        app = input("Enter the name of the app: ")
                        credential_username = input("Enter your username: ")
                        while True:
                            print("Use the following options to select which password you prefer\ncp - Custom Password\nap - Auto-Generated Password\nex - Exit")
                            option = input().lower().strip()

                            if option == "cp":
                                credential_password = input("Enter your password: ")
                                break
                            elif option == "ap":
                                credential_password = Credentials.password()
                                break
                            elif option == "ex":
                                break
                            else:
                                print("Invalid input. Check options and try again.")
                    
                        new_credential = create_credentials(app, credential_username, credential_password)
                        new_credential.save_credentials()

                        print(f"Newly created credential details:\nApp Name: {app}\nUsername: {credential_username}\nPassword: {credential_password}")

                    elif code == "delc":
                        delete_app = input("Enter the app name of the credential you wish to delete: ")
                        Credentials.delete_credential(delete_app)
                        print(f"{delete_app} Credentials has been deleted.")

                    elif code == "dc":
                        if Credentials.display_credentials():
                            for credential in Credentials.display_credentials():
                                print(f"App: {credential.app}\nUsername: {credential.username}\nPassword: {credential.password}\n")
                        else:
                            print("You haven't created any credentials yet.")

                    elif code == "dsc":
                        app_credential = input("Enter app name of the credential you wish to be displayed: ")

                        credential_information = Credentials.display_app_credential(app_credential)

                        if credential_information:
                            print(credential_information)
                        else:
                            "That credential cannot be found. Please try again"
                    
                    elif code == "ex":
                        break
                        
                    else:
                        "Invalid input. Please check the code and try again."

        elif short_code == "ex":
            break

        else:
            print("Invalid input. Please check your entry and try again.")

if __name__ == '__main__':
    main()
