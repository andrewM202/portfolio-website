from flask import Blueprint, request, Flask, render_template, redirect, jsonify 
from flask_login import current_user
from models import Quickchat, db
from flask_mongoengine import MongoEngine
from datetime import datetime

bp = Blueprint("blog", __name__)

@bp.route("/blog")
def blogroute():
    """ Route for blog """
    if current_user.is_authenticated:
        return render_template("blog.html")
    else: 
        return redirect('/')

@bp.route("/blog-editor")
def blogedit():
    """ Edit blog content """
    if current_user.is_authenticated:
        return render_template("blog-editor.html")
    else: 
        return redirect('/')

