import os
from flask import Flask, render_template
from app.blueprints.user_auth_blueprint.user_auth_blueprint import user_auth_blueprint

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("/habits/profile.html")

# Registering the user_auth_blueprint
app.register_blueprint(user_auth_blueprint)


#
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')





