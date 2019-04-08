#!usr/bin/env python3.7
import random
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
    Credentials.save_credentials(credential)


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

    while True:
        short_code = input().upper()
        print("\n")
        print("\n")
        
        
        
        if short_code=='CRT':
            
            print("Create a new Password Locker Acount")
            first_name = input("Enter First Name:").strip()
            last_name = input("Enter Last Name:").strip()
            user_email = input("Enter Email Address:").strip()
            user_password = input("Enter Password:")
            repeat_password = input("Repeat Password:")
            
            
            while user_password!=repeat_password:
                print("")
                print("The passwords did not macth. Please re-enter the password")
                user_password=input("Enter Password:").strip()
                repeat_password = input("Repeat Password:").strip()
            else:
                
                save_user(create_user(first_name,last_name,user_email,user_password))
                print("")
                print(f"New Account created for {first_name}.")
                print("")
                print(f"{first_name}, proceed to create and save your credentials")



        elif short_code=="LOG":
            
            print("+"*60)
            print("Log in using your user-email and password")
            user_email = input("Please enter your registred email:").strip()
            user_password = input("Password:")
            user_exists = verify_user(user_email)

            while True:
                print("")
                print(f"Welcome {first_name}. Please choose an option to continue")
                print("Your options are as follows:")
                print("CR: Create Credentials")
                print("DC: Display Credentials")
                print("CP: Copy Credentials")
                print("EX:Exit Credential Phase")

                credential_choice = input().upper()
                if credential_choice == 'CR':
                    # Create a new credential
                    site_name = input("Enter Site Name:").strip()
                    site_username = input("Enter Username:").strip()
                    print("Pasword: Woudld you like to auto generate a password?. Y - Yes, N - No")
                    pass_choice = input().upper()
                    
                    if pass_choice=='N':
                        site_password = input("Enter site password:")
                    
                    elif pass_choice=='Y':
                        print("Generating password")
                        mixed_text = "423223zxcvb123456nmasdfgh3214jkqwertyu"
                        site_password = "".join(random.choice(mixed_text) for _ in range(10))
                        print("\n")
                        print("Generated passwors is {site_password}.")
                        
                    save_credential(create_credentials(site_name,site_username,site_password))
                    print(f"Credential Created: Site Name: {site_name} - UserName: {site_username} - Password: {site_password}")
                    
                    
                elif credential_choice == 'DC': 
                    # Display credentials
                    print("")
                    for credential in display_credentials(user_email):
                        print(f"Site Name: {credential.site_name} - Account Name: {credential.account_name} - Password: {credential.password}")	
                    
                elif credential_choice == 'CP': 
                    print("")
                    chosen_site = input("Enter the site name for the credential password to copy: ")
                    copy_credentials(chosen_site)
					# print("")
     
                elif credential_choice=='EX':
                    print("")
                    print("You are going back to the main user page")
                    break
                    
                    
                else:
                    print("")
                    print("You don't seem to have any credentials saved yet")
                    print("")



        elif short_code=="EXT":
                print("Leaving the application")
                print("\n")
                break

        else:
            print("Please chose an appropriate code, CRT, LOG and EXT")


if __name__ =="__main__":
    main()
        
        
        
    
        

    

    