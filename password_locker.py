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
    


def main():
    print("\n")
    print("+++++++++++++++ Welcome to your Password Locker ++++++++++++++++")
    print("Please use the follwing shortcodes to:")
    print("1. CRT - to Create a user account")
    print("1. LOG - to Create a user account")
    print("1. EXT - to Create a user account")
    
    short_code = input().upper()
    print("\n")
    print("\n")
    
    if short_code=='CRT':
        print("Create a new Password Locker Acount")
        first_name = input("Enter First Name:").strip()
        last_name = input("Enter Last Name:").strip()
        user_email = input("Enter Email Address:").strip()
        user_password = input("Enter Password:").strip()
        repeat_password = input("Repeat Password:").strip()

        while user_password!=repeat_password:
            print("")
            print("The passwords did not macth. Please re-enter the password")
            user_password=input("Enter Password:").strip()
            repeat_password = input("Repeat Password:").strip()
        else:
            save_user(create_user(first_name,last_name,user_email,user_password))
            print("")
            print(f"New Account created for {first_name}")
            print("")
            print{f"{user_name}, proceed to create and save your credentials"}
            
    elif short_code=="LOG":
        print("+"*60)
        print("Log in using your user-email and password")
        user_email = input("Please enter your registred email:")
        user_password = input("Password:")
    
    
    elif short_code=="EXT":
        print("Leaving the application")
        print("\n")
        break
    
    else:
        print("Please chose an appropriate code, CRT, LOG and EXT")
        
        
        
if if __name__ == "__main__":
    main()
        
        
        
    
        

    

    