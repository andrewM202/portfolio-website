from flask import Blueprint, request, Flask, render_template, redirect, jsonify 
from flask_login import current_user
from models import Quickchat, Article, db
from datetime import date
from resume import allowed_file
from werkzeug.utils import secure_filename
import string, random, os
from app import app

bp = Blueprint("blog", __name__)

@bp.route("/blog")
def blogroute():
    """ Route for blog """
    articles = Article.objects()
    return render_template("blog.html", articles=articles)

@bp.route("/blog-editor")
def blogEdit():
    """ Edit blog content """
    if current_user.is_authenticated:
        return render_template("blog-editor.html")
    else: 
        return redirect('/')

@bp.route("/delete-article")
def deleteArticle():
    pass

@bp.route("/articles")
def seeArticles():
    articles = Article.objects()
    return jsonify(articles)

@bp.route("/process-article", methods=['POST'])
def processArticle():
    """ Process a blog article's content """
    if current_user.is_authenticated:
        if request.method == 'POST':
            articleContent = request.form['ckeditor']
            articleTitle = request.form['title']
            articleDesciption = request.form['description']

            file = request.files['cover-image']
            if file and allowed_file(file.filename):
                # Extension of file
                extension = file.filename.rsplit('.', 1)[1].lower()
                # give the file a random name
                letters = string.ascii_letters
                digits = string.digits
                filename = ''.join(random.choice(letters + digits) for i in range(20)) + "." + extension
                filename = secure_filename(filename)
                # save file to specified directory
                file.save(os.path.join(app.config['BLOG_FOLDER'], filename))
            else:
                return "Invalid File"

            data = Article(
                title = articleTitle,
                content = articleContent,
                coverimage = filename, # The name of the image
                articledesc = articleDesciption,
                date = date.today().strftime("%b %d, %Y")
            )
            data.save()

            return redirect('/blog-editor')
        else: 
            return 'Error 2'#return redirect('/')
    else:
        return 'Error 1'#return redirect('/')


