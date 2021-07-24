from flask import Blueprint, request, Flask, render_template, redirect 
import flask

bp = Blueprint("projects", __name__)

@bp.route("/projects")
def blogroute():
    """ Route for projects """
    
    return render_template("projects.html")

