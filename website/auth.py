import re
from flask import Blueprint

# name the same as the file
auth = Blueprint('auth', __name__)


# These defines login, logout, sign up -roots
@auth.route('/login')
def login():
    return "<p>Login</p>"


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"


@auth.route('/sign-up')
def sing_up():
    return "<p>Sign-up</p>"
