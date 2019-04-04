# Creating a test file for the application:

import unittest# importing the unit test model
from password_locker import User

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

        self.new_user = User("James", "Muriuki", "james@ms.com", "password4you")# create contact object


    def test_instance(self):
        """
        Test instance case to test if the onject initialized properly
        """
        self.assertEqual(self.new_user.first_name, "James")
        self.assertEqual(self.new_user.last_name,"Muriuki")
        self.assertEqual(self.new_user.user_email,"0712345678")
        self.assertEqual(self.new_user.user_password,"james@ms.com")

    def test_save_user(self):
        """
        test_save_user tests if a user has been saved.
        """
        self.new_user.save_contact()#Saving the new user
        self.assertEqual(len(User.user_list),1)


