from flask import Flask, render_template, Blueprint
from config import Config
from flask_socketio import SocketIO
from flask_migrate import Migrate
from flask_mail import Mail
from models import db, login
from flask_sitemap import Sitemap

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

# Initialize XML sitemap 
ext = Sitemap(app=app)

# initialize the mongoengine database
db.init_app(app)

# Create a Flask-Mail instance
mail = Mail(app)

# Create a socketio instance
socketio = SocketIO(app)

# Create Flask-Login instance
login.init_app(app)
login.login_view = 'login'

# Register Routes / Import Blueprints
import homepage
app.register_blueprint(homepage.bp)

import blog
app.register_blueprint(blog.bp)

import resume
app.register_blueprint(resume.bp)

import mail
app.register_blueprint(mail.bp)

import login 
app.register_blueprint(login.bp)

if __name__ == "__main__":
    socketio.run(app)
