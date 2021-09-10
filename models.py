from flask import Flask
from flask_mongoengine import MongoEngine

db = MongoEngine()

# Initializing test class with a document
class Quickchat(db.Document):
    """ Test Class """
    name = db.StringField(required=True)
    message = db.StringField(required=True)
    datetime = db.DateTimeField()
