from flask import Blueprint, request, Flask, render_template, redirect, jsonify
from flask_login import current_user
from models import Quickchat, Article
from datetime import date, datetime
from resume import allowed_file
from werkzeug.utils import secure_filename
import string, random, os
from app import app
# For some reason need this for saving DB images
from PIL import Image

bp = Blueprint("blog", __name__)

def render_images():
    """ Initializes the images from database
    into local storage """
    articles = Article.objects()
    for art in articles:
        # Save image to directory if it 
        # is not already in directory
        # path is path to file
        path = os.path.join(app.config['BLOG_FOLDER'], art.coverimage_name)
        if not os.path.isfile(path):
            with Image.open(art.coverimage) as im:
                im.save(os.path.join(app.config['BLOG_FOLDER'] + art.coverimage_name), 'JPEG')

@bp.route("/blog")
def blogroute():
    """ Route for blog """
    articles = Article.objects()
    # In Heroku, dynamically added files into a folder are not permanent,
    # and are lost upon the dynamos stopping or updating. So, we need 
    # to load all of our files into the blog folder from out mongodb database
    # which is what render_images() does
    render_images()
    return render_template("blog.html", articles=articles)

@bp.route("/blog-editor")
def blogEdit():
    """ Edit blog content """
    if current_user.is_authenticated:
        return render_template("blog-editor.html")
    else: 
        return redirect('/')

@bp.route("/blog/delete-article/", methods=["POST"])
def deleteArticle():
    if current_user.is_authenticated:
        articleid = request.form['article-id']
        # print(articleid)
        print(request.form)
        article = Article.objects.get(id=articleid)
        article.delete()
        return redirect('/blog')
    else:
        return redirect('/blog/')

@bp.route("/articles")
def seeArticles():
    articles = Article.objects()
    return jsonify(articles)

@bp.route("/blog/article/<id>")
def seeArticle(id):
    """ Returns a single article """
    article = Article.objects(id=str(id))[0]
    # get adobe API key
    adobe_id = os.environ.get('ADOBE_ID')
    return render_template("article.html", article=article, adobe_id=adobe_id)

@bp.route("/process-article", methods=['POST'])
def processArticle():
    """ Process a blog article's content """
    if current_user.is_authenticated:
        if request.method == 'POST':
            # Create mongoengine connection 
            data = Article()

            articleContent = request.form['ckeditor']
            articleTitle = request.form['title'].title()
            articleDesciption = request.form['description'] 

            article_pdf_filename = None
            if request.files['uploaded-article'] and (articleContent is None or articleContent == ""):
                article_pdf = request.files['uploaded-article']
                if article_pdf and allowed_file(article_pdf.filename):
                    date.uploaded_content=article_pdf
                else:
                    return "Not allowed file type"

            file = request.files['cover-image']
            if file and allowed_file(file.filename):
                # Extension of file
                extension = file.filename.rsplit('.', 1)[1].lower()
                # give the file a random name
                letters = string.ascii_letters
                digits = string.digits
                filename = ''.join(random.choice(letters + digits) for i in range(20)) + "." + extension
                filename = secure_filename(filename)
                data.coverimage.replace(file, filename=filename)
                data.coverimage_name = filename + '.' + extension
                # save file to specified directory
                file.save(os.path.join(app.config['BLOG_FOLDER'], filename))
            else:
                return "Invalid File"

            data.title = articleTitle
            data.content = articleContent
            data.articledesc = articleDesciption
            data.date = date.today().strftime("%b %d, %Y")
            data.formatted_date = str(date.today().strftime("%b %d, %Y"))

            data.save()

            return redirect('/blog-editor')
        else: 
            return 'Error 2'#return redirect('/')
    else:
        return 'Error 1'#return redirect('/')


