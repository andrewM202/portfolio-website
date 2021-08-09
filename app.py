from flask import Flask, render_template, Blueprint
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from flask_migrate import Migrate
from flask_mail import Mail
from models import db, Test

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

# Configure MongoDB Database
app.config['MONGODB_SETTINGS'] = {
    'db': 'portfolio_db',
    'host': 'localhost',
    'port': 27017
}

db.init_app(app)

# Create a Flask-Mail instance
mail = Mail(app)

# Register Routes / Import Blueprints
import homepage
app.register_blueprint(homepage.bp)

import blog
app.register_blueprint(blog.bp)

import projects
app.register_blueprint(projects.bp)

import resume
app.register_blueprint(resume.bp)

import mail
app.register_blueprint(mail.bp)

socketio = SocketIO(app)

if __name__ == "__main__":
    socketio.run(app)
