from flask import Flask
from mongoengine import *
from flask_login import UserMixin, LoginManager

db = connect(host="mongodb://127.0.0.1:27017/portfolio-website")

login = LoginManager()

# Initializing test class with a document
class Quickchat(Document):
    """ Quickchats """
    name = StringField(required=True)
    message = StringField(required=True)
    datetime = DateTimeField()

class Article(Document):
    """ Articles for blog """
    title = StringField(required=True)
    content = StringField(required=True)
    # uploaded_content = db.StringField()
    # coverimage = db.StringField(required=True)
    uploaded_content = StringField()
    coverimage = ImageField(required=True)
    coverimage_name = StringField(required=True)
    articledesc = StringField(required=True)
    date = DateField(required=True)
    formatted_date = StringField(required=True)

class User(Document):
    """ Login Information """
    username = StringField(required=True)
    password = StringField(required=True)

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