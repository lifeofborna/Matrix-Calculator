from repositories.user_repository import UserRepository


class UserService:

    def __init__(self, test=""):
        self.test = test
        self.user_repository = UserRepository(test=str(self.test))

    def check_username(self, username):
        size_username = len(username)
        if size_username > 15 or size_username == 0:
            return False
        return True

    def check_password(self, password):
        if len(password) < 5:
            return False
        return True

    def create_user(self, username, password):
        valid_username = self.check_username(username)
        valid_password = self.check_password(password)

        if valid_username is False:
            return "Invalid username, please use a valid username! max (15 characters)"

        if valid_password is False:
            return "Please use a password higher 5 characters!"

        if self.user_repository.create_user(username, password) is False:
            return "The username is not unique!"

        return True

    def login_user(self, username, password):
        login_operation = self.user_repository.login_user(username, password)

        if login_operation:
            return True

        return False

    def remove_users(self):
        self.user_repository.drop_table()
