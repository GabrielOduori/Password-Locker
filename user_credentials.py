# Creating the required classes for the application
import random
import string
import pyperclip

# Global Variables
# global users_list
# global credentials_list

class User:
    """
    A class that generates new User
    first_name: New contact first name.
    last_name : New contact last name.
    user_email: New contact phone number.
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
        
    @classmethod    
    def user_exists(cls, user_email):
        """
        user_exists method checks if a user with the email provided 
        already exists in the users_list
        """
        for email in cls.users_list:
            if email.user_email == user_email:
                return True
            return False
        
    @classmethod
    def authenticate_password(cls,user_password):
        """
        authenticate_password method checks if a user's password is
        legit
        """
        for password in cls.users_list:
            if password.user_password==user_password:
                return True
            return False
        
        
1

class Credentials:
    """ 
    A class that generates new Credentials as follows:
    cred_username:Credential username
    site_name: New contact first name.
    site_username: Username used e.g Twitter handler
    site_password : Password for login into the site.
    """

    credentials_list = [] # Empty list of credentials
    user_credentials_list = []
    
    def __init__(self, site_name, site_username, site_password):
        self.site_name = site_name
        self.site_username = site_username
        self.site_password = site_password
        

    def save_credentials(self):
        """
        save_credentials saves a new credential in the list of 
        credentials
        """
        Credentials.credentials_list.append(self)
        
        
    def delete_credentials(self):
        '''
        delete_credential method deletes a saved credential from a
        user credential list
        '''
        Credentials.credentials_list.remove(self)
        
        
    @classmethod    
    def authenticate_user(cls,user_email):
        """
        authenticate_user method checks if user exists and that have 
        a valid password
        """
        pass

    @classmethod
    def display_credentials(cls):

        """
        display_credentials method displays the list of already saved credentials
        # """
        return cls.user_credentials_list
        # user_credentials_list = []
        # for credential in cls.credentials_list:
        #     if credential.cred_username == cred_username:
        #         user_credentials_list.append(credential)
        # return user_credentials_list
    
    
    # def generate_password(self, size=10, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
    #     """
    #     generate_password helps in generating password for the user if the option is choosen
        
    #     """
    #     generated_pass = ''.join(random.choice(char)for _ in range(size))
    #     return generated_pass
    
    
    # @classmethod
    # def find_by_website(cls,site_name):
    #     """
    #     find_by_website method returns credentials saved by website
    #     """
    #     for credential in cls.credentials_list:
    #         if credential.site_name ==site_name:
    #             return credential
    
    
    @classmethod
    def copy_credentials(cls,site_name):
        """
        copy_password method hels user copy the auto-generated password for a 
        specific website
        """
        credential_found = Credentials.find_by_website(site_name)
        return pyperclip.copy(credential_found.site_password)


    






