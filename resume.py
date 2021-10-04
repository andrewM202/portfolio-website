from flask import Blueprint, request, Flask, render_template, redirect 
from flask_login import current_user
from werkzeug.utils import secure_filename
import os
from app import app

bp = Blueprint("resume", __name__)

@bp.route("/resume-upload")
def uploadresume():
    """ Rendering resume upload template """
    if current_user.is_authenticated:
        return render_template("resume-upload.html")
    else:
        return redirect('/')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@bp.route("/resume-process", methods=['POST', 'GET'])
def resumeProcess():
    """ Processing uploaded resume """
    if current_user.is_authenticated:
        if request.method == 'POST':
            file = request.files['File']
            if file and allowed_file(file.filename):
                # change filename name
                file.filename = 'resume.pdf'
                filename = secure_filename(file.filename)
                # save file to specified directory
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                return redirect('/')
            else:
                return "Invalid File"
        else:
            return redirect('/resume-upload')
    else:
        return redirect('/')

