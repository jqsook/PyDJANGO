from flask import render_template, request, flash
from flask import Blueprint

# name the same as the file
auth = Blueprint('auth', __name__)

# This defines login, logout, sign up


@auth.route('/login', methods=['GET', 'POST'])
def login():

    return render_template("/log_in.html", boolean=True)


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 4 characters', category='error')
        elif len(firstName) < 2:
            flash('First Name must be greater than 3 characters', category='error')
        elif password1 != password2:
            flash('Passwords do not match', category='error')
        elif len(password1) < 7:
            flash('Password must be greater than 8 characters', category='error')
        else:
            flash('Account Created', category='success')

    return render_template("/sign_up.html")
