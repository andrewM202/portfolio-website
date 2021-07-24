from flask import Blueprint, request, Flask, render_template, redirect 
import flask

bp = Blueprint("blog", __name__)

@bp.route("/blog")
def blogroute():
    """ Route for blog """
    
    return render_template("blog.html")
