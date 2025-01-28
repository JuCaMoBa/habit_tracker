# This file contains the code to interact with the database for user authentication
# It contains the UserAuthRepository class which is used to interact with the database
# It contains the insert_user method to insert a user into the database
# It contains the select_user method to select a user from the database

from database.database_connection import DBConnection


class UserAuthRepository:

    def __init__(self, db:DBConnection): # code to initialize the database connection):
        self.db = db

    def insert_user(self, user_credentials): # code to insert user into database
        # code to insert user into database
        print(user_credentials)
        return 'User inserted successfully'
    
    def select_user(self, user_credentials): # code to select user from database
        # code to select user from database
        return 'User selected successfully'
        




