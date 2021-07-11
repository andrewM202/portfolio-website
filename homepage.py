from flask import Blueprint, render_template

bp = Blueprint("homepage", __name__)

@bp.route('/')
def load_homepage():
    """ Home page for portfolio """
    return render_template("index.html")
