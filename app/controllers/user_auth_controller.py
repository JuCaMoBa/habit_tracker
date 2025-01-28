# This file contains the controller functions for user authentication
# It contains the login, register, register_render_template, login_render_template, logout, forgot_password, reset_password, change_password, verify_email, resend_verification_email, delete_account, and update_profile functions

from flask import flash, render_template, request, session
from database.database_connection import DBConnection
from respositories.user_auth_repositoriy import UserAuthRepository
from services.user_auth_services import UserAuthServices

db_connection = DBConnection()
user_auth_repository = UserAuthRepository(db_connection)
user_auth_services = UserAuthServices(user_auth_repository)

def login():
    user_credentials = {
        'email' : request.form['username'],
        'password' : request.form['password'],
    }

    user = user_auth_services.check_login_user(user_credentials)
    if user:
        session['user'] = user
        return 'User logged in successfully'

    return 'Invalid email or password'

def register():
    user_credentials = {
        'name' : request.form['name'],
        'email' : request.form['email'],
        'password' : request.form['password'],
        'confirm_password' : request.form['confirm_password'],
    }

    user = user_auth_services.check_user_exists(user_credentials)
    if user:
        flash('User already exists')
        return 'User already exists go to login page and login with your email and password'
    else: 
        user_auth_services.create_user(user_credentials)
        flash('User registered successfully go to login page and login with your email and password')   
        return 'User registered successfully'

def register_render_template():
    # code to render registration template
    return render_template('/user_auth/register.html')

def login_render_template():
    # code to render login template
    return render_template('/user_auth/login.html')

def logout():
    # code to logout user
    return 'User logged out successfully'

def forgot_password():
    # code to send password reset link
    return 'Password reset link sent successfully'

def reset_password():
    # code to reset password
    return 'Password reset successfully'

def change_password():
    # code to change password
    return 'Password changed successfully'

def verify_email():
    # code to verify email
    return 'Email verified successfully'

def resend_verification_email():
    # code to resend verification email
    return 'Verification email resent successfully'

def delete_account():
    # code to delete account
    return 'Account deleted successfully'

def update_profile():
    # code to update user profile
    return 'Profile updated successfully'



