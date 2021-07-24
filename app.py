from flask import Flask, render_template, Blueprint
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from flask_migrate import Migrate
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

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
