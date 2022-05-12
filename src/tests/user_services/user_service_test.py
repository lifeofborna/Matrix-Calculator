import unittest
from services.user_service import UserService


class TestUserService(unittest.TestCase):
    def setUp(self):

        self.user_service = UserService(test="test.db")
        self.user_service.remove_users()

    def test_check_if_create_user_valid(self):
        result = self.user_service.create_user("Joe Mama", "whoisjoe?")
        self.assertEqual(str(result), "True")

    def test_check_if_create_user_not_unique(self):
        self.user_service.create_user("Joe Mama", "whoisjoe?")
        result = self.user_service.create_user("Joe Mama", "whoisjoe?")
        self.assertEqual(str(result), "The username is not unique!")

    def test_check_if_create_user_invalid_password(self):
        result = self.user_service.create_user("Joe Mama", "joe")
        self.assertEqual(
            str(result), "Please use a password higher 5 characters!")

    def test_check_if_create_user_invalid_username(self):
        result = self.user_service.create_user(
            "ILOOOOOOOOOOOOOOOOOOOOOOOOOOOVE", "joe")
        self.assertEqual(str(
            result), "Invalid username, please use a valid username! max (15 characters)")

    def test_check_if_can_login(self):
        self.user_service.create_user("Joe Mama", "whoisjoe?")
        result = self.user_service.login_user("Joe Mama", "whoisjoe?")
        self.assertEqual(str(result), "True")

    def test_check_if_cant_login_wrong_password(self):
        self.user_service.create_user("Joe Mama", "whoisjoe?")
        result = self.user_service.login_user("Joe Mama", "iforgotmypassword")
        self.assertEqual(str(result), "False")

    def test_check_if_cant_login_wrong_username(self):
        self.user_service.create_user("Joe Mama", "whoisjoe?")
        result = self.user_service.login_user("Joe Mama", "iforgotmypassword")
        self.assertEqual(str(result), "False")
