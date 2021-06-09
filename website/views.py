from flask import Blueprint, render_template

# name the same as the file
views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html")
