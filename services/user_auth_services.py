# This file contains the services for user authentication

from respositories.user_auth_repositoriy import UserAuthRepository


class UserAuthServices:
    def __init__(self, user_auth_repository: UserAuthRepository): # code to initialize user_auth_repository  
        self.user_auth_repository = user_auth_repository           

    def create_user(self, user_credentials): # code to insert user into database    
        return self.user_auth_repository.insert_user(user_credentials) 

    def check_login_user(self, user_credentials): # code to check if user credentials are correct
        return self.user_auth_repository.select_user(user_credentials) 
    
    def check_user_exists(self, user_credentials): # code to check if user exists in database
        return self.user_auth_repository.select_user(user_credentials) 
    

    