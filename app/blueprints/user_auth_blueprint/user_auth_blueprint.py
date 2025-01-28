# Desc: Blueprint for user authentication routes

from flask import Blueprint

user_auth_blueprint = Blueprint(
    'user_auth',
    __name__,
    url_prefix='/user_auth',
    template_folder='templates', 
    static_folder='static'
)

from . import user_auth_routes