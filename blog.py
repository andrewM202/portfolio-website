from flask import Blueprint, request, Flask, render_template, redirect, jsonify 
from flask_login import current_user
from models import Quickchat, db
from datetime import datetime

bp = Blueprint("blog", __name__)

@bp.route("/blog")
def blogroute():
    """ Route for blog """
    return render_template("blog.html")

@bp.route("/blog-editor")
def blogEdit():
    """ Edit blog content """
    if current_user.is_authenticated:
        return render_template("blog-editor.html")
    else: 
        return redirect('/')

@bp.route("delete-article")
def deleteArticle():
    pass

@bp.route("/process-article", methods=['POST'])
def processArticle():
    """ Process a blog article's content """
    if current_user.is_authenticated:
        if request.method == 'POST':
            data = request.form['ckeditor']
            articleTitle = str(request.form['title'])
            print(articleTitle)
            print(data)
            return redirect('/blog-editor')
        else: 
            return redirect('/')
    else:
        return redirect('/')


