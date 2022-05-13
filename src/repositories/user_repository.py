import sqlite3


class UserRepository:

    '''
    This class will execute different SQL operations on a database.
    Functionality to create/login/cleartable.

    '''

    def __init__(self, test=""):

        self._create_database = test

        if test == "":
            self._create_database = 'database.db'

        with sqlite3.connect(self._create_database) as self._database:
            self._cursor = self._database.cursor()

        self._cursor.execute(
            '''CREATE TABLE IF NOT EXISTS user
            (username TEXT NOT NULL PRIMARY KEY,password TEXT NOT NULL);''')
        self._database.commit()

    def create_user(self, user, password):
        '''
        create a new user into database

        Args:
            user,password to set in to the database

        Returns:
            True if user has been added to database else False.

        '''

        taken_user = ('SELECT username FROM User WHERE username = ?')
        self._cursor.execute(taken_user, [(user)])
        found_user = self._cursor.fetchall()

        if found_user:
            return False

        create_account = 'INSERT INTO user(username,password) VALUES(?,?)'
        self._cursor.execute(create_account, [(user), (password)])

        self._database.commit()
        return True

    def login_user(self, username, password):
        '''
        login a user to the system

        Args:
            username,password to check if credentials match in the database

        Returns:
            True if login with the credentials is successfull else False.
        '''

        search_user = (
            'SELECT * FROM user WHERE username = ? AND password = ?')
        self._cursor.execute(
            search_user, [(username), (password)])
        res = self._cursor.fetchall()

        if res:
            return True

        return False

    def clear_table(self):
        '''
        clear the database by deleting everything from user
        '''
        self._cursor.execute("DELETE FROM user")
