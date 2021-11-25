from flask import Flask
from flask_mongoengine import MongoEngine
from flask_login import UserMixin, LoginManager

db = MongoEngine()
login = LoginManager()

# Initializing test class with a document
class Quickchat(db.Document):
    """ Quickchats """
    name = db.StringField(required=True)
    message = db.StringField(required=True)
    datetime = db.DateTimeField()

class Article(db.Document):
    """ Articles for blog """
    title = db.StringField(required=True)
    content = db.StringField(required=True)
    coverimage = db.StringField(required=True)
    articledesc = db.StringField(required=True)
    date = db.DateField(required=True)
    formatted_date = db.StringField(required=True)

class User(db.Document):
    """ Login Information """
    username = db.StringField(required=True)
    password = db.StringField(required=True)

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return User.objects().first()

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

@login.user_loader
def load_user(user_id):
    return User.objects().first()
