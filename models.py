from flask import Flask
from flask_mongoengine import MongoEngine

db = MongoEngine()

# Initializing test class with a document
class Quickchat(db.Document):
    """ Quickchats """
    name = db.StringField(required=True)
    message = db.StringField(required=True)
    datetime = db.DateTimeField()

class login(db.Document):
    """ Login Information """
    username = db.StringField(required=True)
    password = db.StringField(required=True)