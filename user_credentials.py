# Creating the required classes for the application
import random
import string

# Global Variables
# global users_list
# global credentials_list

class User:
    """
    A class that generates new User
    first_name: New contact first name.
    last_name : New contact last name.
    email_address: New contact phone number.
    user_password : New contact email address.
    """

    users_list = []

    def __init__(self, fist_name, last_name, user_email, user_password):

        self.first_name = fist_name
        self.last_name = last_name
        self.user_email = user_email
        self.user_password = user_password

    def save_user(self):

        """
        save_user method saves a new user into the user list
        """
        User.users_list.append(self)

    def delete_user(self):
        """
        delete_user deletes an existing user from the userlist
        """
        User.users_list.remove(self)
        
    # def user_exists(self,cls, user_email):
    #     """
    #     user_exists method checks if a user with the email provided 
    #     already exists in the users_list
    #     """
    #     for email in cls.users_list:
    #         if user_email.user_email == user_email:
    #             return True
    #         return False
        
    # def authenticate_password(self,cls,user_password):
    #     """
    #     authenticate_password method authenticates users password
    #     """
    #     for password in cls.users_list:
    #         if password.user_password==user_password:
    #             return True
    #         return False
        
        
1

class Credentials:
    """ 
    A class that generates new Credentials as follows:
    site_name: New contact first name.
    site_username: Username used e.g Twitter handler
    site_password : Password for login into the site.
    """

    credentials_list = [] # Empty list of credentials
    
    def __init__(self, site_name, site_username, site_password):
        self.site_name = site_name
        self.site_username = site_username
        self.user_password = site_password
        

    def save_credentials(self):
        """
        save_credentials saves a new credential in the list of 
        credentials
        """
        Credentials.credentials_list.append(self)
        
        
#     @classmethod
#     def check_current_user(cls, user_email):
#         current_user = ""
#         for user in User.users_list:
#             if user.user_email == user_email and user.user_password == password:
#                 current_user = user.first_name
#         return current_user

#     def generate_password(self, size=10, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
#         """
#         generate_password helps in generating password for the user if the option is choosen
        
#         """
#         generated_pass = ''.join(random.choice(char)for _ in range(size))
#         return generated_pass

    # @classmethod
    # def display_credentials(cls):

    #     """
    #     display_credentials method displays the list of already saved credentials
    #     """
    #     # user_credentials_list = []
    #     # for credential in cls.credentials_list:
    #     #     if credential.user_email == user_email:
    #     #         user_credentials_list.append(credential)
    #     # return user_credentials_list
    #     return cls.credentials_list(cls)


# def delete_credential(self):
#     '''
#     delete_credential method deletes a saved credential from a
#     user credential list
#     '''
#     Credentials.credentials_list.remove()




