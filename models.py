from flask import Flask
from flask_mongoengine import MongoEngine

db = MongoEngine()

# Initializing test class with a document
class Test(db.Document):
    """ Test Class """
    name = db.StringField()
    email = db.StringField()
