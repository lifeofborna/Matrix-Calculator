from repositories.user_repository import UserRepository


class UserService:
    '''
    This class handles the logic of creating/registering a user or removing all of the users.

    '''

    def __init__(self, test=""):
        self.test = test
        self.user_repository = UserRepository(test=str(self.test))

    def check_username(self, username):
        '''
        checks if username is valid

        Args:
            username

        Returns:
            True if username is not empty and size is less than 15 characters. Else false

        '''
        size_username = len(username)
        if size_username > 15 or size_username == 0:
            return False
        return True

    def check_password(self, password):
        '''
        checks if password is valid

        Args:
            username

        Returns:
            True if password size is higher than 5 characters. Else false

        '''
        if len(password) < 5:
            return False
        return True

    def create_user(self, username, password):
        '''
        Checks if username/password valid.
        If valid calls user_repository to save the username/password.

        Args:
            username, password

        Returns:
            A string that consist with appropriate error message or True if user has been created.

        '''
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
        '''
        Checks if username,password match in the database via user_repository.

        Args:
            username,password

        Returns:
            True if correct credentials else False.

        '''
        login_operation = self.user_repository.login_user(username, password)

        if login_operation:
            return True

        return False

    def remove_users(self):
        '''
        Clears user table via user_repository.

        '''
        self.user_repository.clear_table()
