# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from flask_login import UserMixin
from werkzeug.security import check_password_hash

from emerson import db


# Define a base model for other database tables to inherit
class AdminUser(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(256), unique=True, nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    active = db.Column("is_active", db.Boolean(), nullable=False, server_default="0")

    def __init__(self, username, email, password, active):
        self.username = username
        self.email = email
        self.password = password
        self.active = active

    def __repr__(self):
        return '<AdminUser %r>' % self.username

    def get_id(self):
        return self.id

    def check_password(self, password):
        return check_password_hash(self.password, password)
