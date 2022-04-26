import unittest

from repositories.user_repository import UserRepository


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.user_repository = UserRepository()

    def test_check_if_user_created(self):
        user = 'donald'
        password = 'trump'
        try:
            self.user_repository.delete_user(user)
        except:
            'correct'

        result = self.user_repository.create_user(user, password)

        self.assertEqual(str(result), "True")

    def test_check_if_user_created_not_unique(self):
        user = 'donald'
        password = 'trump'

        result = self.user_repository.create_user(user, password)

        self.assertEqual(str(result), "False")
