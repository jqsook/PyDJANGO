from flask import render_template
from flask import Blueprint

# name the same as the file
auth = Blueprint('auth', __name__)

# This defines login, logout, sign up


@auth.route('/login')
def login():
    return render_template("/log_in.html")


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"


@auth.route('/sign-up')
def sign_up():
    return render_template("/sign_up.html")
