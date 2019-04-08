# Creating a test file for the application:

import unittest  # importing the unit test model
from user_credentials import User, Credentials 
import pyperclip

class TestUser(unittest.TestCase):

    """
    Test class that defines te test case for the User behavior
    Args:
        unittest.TestCase: Test class that helps create the test case
    """

    def setUp(self):

        """
        Set up method to run before each test case
        """

        self.new_user = User("Gabriel","Oduori","gabriel.oduori@gmail.com", "gabriel@moringa")# create contact object

    def test_instance(self):
        """
        Test instance case to test if the object initialized properly
        """
        self.assertEqual(self.new_user.first_name, "Gabriel")
        self.assertEqual(self.new_user.last_name,"Oduori")
        self.assertEqual(self.new_user.user_email,"gabriel.oduori@gmail.com")
        self.assertEqual(self.new_user.user_password,"password4me")
    
    def test_save_user(self):
        """
        test_save_user test case to test if the contact object is saved into
        the user list
        """
        self.new_user.save_user()
        self.assertEqual(len(User.users_list),1)
    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run.
        """
        User.users_list=[]
        
    def test_save_multiple_users(self):
        """
        test_save_multiple_users check if we can save multiple user
        objects to our user_list
        """
        self.new_user.save_user()
        test_user= User("FirstName","LastName","test@mail.com", "AnotherPassword")
        test_user.save_user()
        self.assertEqual(len(User.users_list),2)
        
        
    def test_delete_user(self):
        """
        test_delete_user method tests if we can remove a user from the user_list
        """
        self.new_user.save_user()
        test_user= User("FirstName","LastName","test@mail.com", "AnotherPassword")
        test_user.save_user()
        
        self.new_user.delete_user()
        self.assertEqual(len(User.users_list),1)
        
    def test_user_exists(self):
        """
        test_user_exists test case to test if the user exists in the
        list of users.
        """
        self.new_user = User("Gabriel","Oduori","gabriel.oduori@gmail.com", "password4me")# create contact object
        self.new_user.save_user()
        user_exists = User.user_exists("gabriel.oduori@gmail.com")
        self.assertTrue(user_exists)
        
    def test_authenticate_password(self):
        """
        test_authenticate_password checks if the password exists for login purposes
        """
        self.new_user = User("Gabriel","Oduori","gabriel.oduori@gmail.com", "password4me")# create contact object
        self.new_user.save_user()
        true_password = User.authenticate_password("password4me")
        self.assertTrue(true_password)

        
class TestCredentials(unittest.TestCase):
    """
    Test class that defines te test case for the Credentials behavior
    Args:
        unittest.TestCase: Test class that helps create the test case
    """
#     def test_check_current_user(self):
#         """
#         test_check_current_user checks the current user 
#         """
#         self.new_user = User("Gabriel","Oduori","gabriel.oduori@gmail.com","another_password")
#         self.new_user.save_user()
#         another_user = User("Mary","Kamaa","mary@protonmail.com","email@Password")

#         for user in User.users_list:
#             if user.user_email == another_user.user_email and user.user_password == another_user.user_password:
#                 current_user = user.first_name
#         return current_user
#         self.assertEqual(current_user,Credentials.check_current_user(another_user.user_password, another_user.user_email))


    def setUp(self):
        """
        SetUp method to create an acounts Credentials before each test case
        """
        self.new_credential = Credentials("Twitter","goduori","tWitTer_pass")

    def test_instance(self):
        """
        test_instance to test initialization of the Credentials instance
        """
        self.assertEqual(self.new_credential.site_name,'Twitter')
        self.assertEqual(self.new_credential.site_username,'goduori')
        self.assertEqual(self.new_credential.site_password,'tWitTer_pass')


    def test_save_credentials(self):
        """
        test_save_credentials tests if the credentials created 
        are saved in the credentials list
        """
        self.new_credential.save_credentials()
        twitter = Credentials("Twitter","goduori","tWitTer_pass")
        twitter.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)
    
    def tearDown(self):
        """
        This cleans up while after running the tests
        """
        Credentials.credentials_list=[]
    
    def test_save_multiple_credentials(self):
        """
        test_save_multiple_users check if we can save multiple credential
        objects to our user_list
        """
        self.new_credential.save_credentials()
        test_credential= Credentials("Twitter","goduori","tWitTer_pass")
        test_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)
        
        
    def test_delete_credentials(self):
        """
        test_delete_credentials checks if we can remove a credential from 
        the credential list
        """
        self.new_credential.save_credentials()
        test_credential = Credentials('Twitter', 'goduori','tWitTer_pass')
        test_credential.save_credentials()
        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)
        

    def test_display_credentials(self):
        """
        test_display_credentials checks if the display credential method
        is displaying the data correctly
        """
        self.new_credential.save_credentials()
        Twitter_credential = Credentials('Twitter','goduori','tWitTer_pass')
        Twitter_credential.save_credentials()
        
        FaceBook_credential = Credentials('Facebook','gabriel.oduori','pswdF200')
        FaceBook_credential.save_credentials()
        
        self.assertEqual(len(Credentials.display_credentials(Twitter_credential)),2)
        
        
    def test_copy_password(self):
        """
        test_copy_password test to confirm that the user can copy a password for 
        a given website
        """
        self.new_credential.save_credentials()
        copy_credentials = Credentials('Facebook','gabriel.oduori','pswdF200')
        copy_credentials.save_credentials()
        Credentials.copy_password("Facebook")
        self.assertEqual(self.new_credential.site_password,pyperclip.paste())
        

if __name__ =='__main__':
    unittest.main()

