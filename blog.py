from flask import Blueprint, request, Flask, render_template, redirect, jsonify 
import flask
from models import Quickchat, db
from flask_mongoengine import MongoEngine
from datetime import datetime

bp = Blueprint("blog", __name__)

@bp.route("/blog")
def blogroute():
    """ Route for blog """
    
    return render_template("blog.html")

