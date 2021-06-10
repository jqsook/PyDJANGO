from datetime import timezone
from enum import unique
from . import db
from flask_login import UserMixin
# This automatically makes the date for any new items stored in the database
from sqlalchemy.sql import func


# This sets up the generic object that is going to be saved in the database- for my app/CCC-C this will be the generic model of the items that can be stored in the database (think Craig's list)


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # This references a key in another column - A one to many relationship- One user with many notes. This foreign key is the id that is on all the children and it references the parent user.
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):  # The Code following sets up the columns
    id = db.Column(db.Integer, primary_key=True)
    # Unique makes it so there can only be one email and no other users can share this email.
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    # This is the list that carries all the children/Notes the user creates. Capital letter here is mandatory- SQLAlchemy
    notes = db.relationship('Note')
