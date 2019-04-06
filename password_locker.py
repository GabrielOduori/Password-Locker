#!usr/bin/env python3.7
from user_credentials import User, Credentials

def create_user(fist_name, last_name, user_email, user_password):
    """
    create_user creates a new user
    """
    new_user = User(fist_name, last_name, user_email, user_password)
    return new_user

def save_user(user):
    """
    save_user saves a new user to the users list
    """
    User.save_user(user)
    
def verify_user(user):
    """
    verify_user
    """
    pass

def generate_password():
    """
    generate_password generates a new auto-password
    """
    pass
def create_credentials(site_name, site_username, site_password):
    """
    """
    new_credential = Credentials(site_name, site_username, site_password)
    return new_credential

def save_credential(credential):
    """
    """
    Credentials.save_credential(credential)
    
    
    
def display_credentials(site_email):
    """
    display_credentials displays credentials
    """
    return Credentials.display_credentials(site_email)
    
