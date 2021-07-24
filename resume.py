from flask import Blueprint, request, Flask, render_template, redirect 
import flask

bp = Blueprint("resume", __name__)

@bp.route("/resume")
def blogroute():
    """ Route for resume """
    
    return render_template("resume.html")

