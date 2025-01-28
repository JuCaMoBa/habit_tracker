# Desc: Routes for the user_auth_blueprint

from .user_auth_blueprint import user_auth_blueprint
from app.controllers.user_auth_controller import (
    login,
    register,
    register_render_template,
    login_render_template
)

user_auth_blueprint.add_url_rule(
    '/login', 
    view_func=login, 
    methods=['POST'],
)

user_auth_blueprint.add_url_rule(
    '/register', 
    view_func= register, 
    methods=['POST'],
)

user_auth_blueprint.add_url_rule(
    '/register', 
    view_func= register_render_template, 
    methods=['GET'],
)

user_auth_blueprint.add_url_rule(
    '/login', 
    view_func= login_render_template, 
    methods=['GET'],
)
