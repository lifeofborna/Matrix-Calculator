import sqlite3

with sqlite3.connect('database.db') as database:
    cursor = database.cursor()


cursor.execute(
    'CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL PRIMARY KEY,password TEXT NOT NULL);')
database.commit()
database.close()


class UserRepository:

    def create_user(self, user, password):
        '''
        create a new user into database

        Args:
            user,password to set in to the database

        Returns:
            True if user has been added to database else False.

        '''
        with sqlite3.connect('database.db') as database_operation:
            cursor_operation = database_operation.cursor()

        taken_user = ('SELECT username FROM User WHERE username = ?')
        cursor_operation.execute(taken_user, [(user)])
        found_user = cursor_operation.fetchall()

        if found_user:
            return False

        create_account = 'INSERT INTO user(username,password) VALUES(?,?)'
        cursor_operation.execute(create_account, [(user), (password)])

        database_operation.commit()
        return True

    def login_user(self, username, password):
        '''
        login a user to the system

        Args:
            username,password to check if credentials match in the database

        Returns:
            True if login with the credentials is successfull else False.
        '''
        with sqlite3.connect('database.db') as database_operation:
            cursor_operation = database_operation.cursor()

        search_user = (
            'SELECT * FROM user WHERE username = ? AND password = ?')
        cursor_operation.execute(
            search_user, [(username), (password)])
        res = cursor_operation.fetchall()

        if res:
            return True

        return False

    def delete_user(self, user):
        '''
        Delete a user from the database

        Args:
            user: Given user to delete from database
        '''

        with sqlite3.connect('database.db') as database_operation:
            cursor_operation = database_operation.cursor()
        sql_delete_user = ('DELETE FROM user WHERE username = ?')
        cursor_operation.execute(sql_delete_user, [(user)])
        database_operation.commit()
