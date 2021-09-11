from flask import Blueprint, request, Flask, render_template, redirect 
from werkzeug.utils import secure_filename
import os
from app import app

bp = Blueprint("resume", __name__)

@bp.route("/resume")
def viewresume():
    """ Route for resume """

    return render_template("resume.html")

@bp.route("/resume-upload")
def uploadresume():
    """ Rendering resume upload template """
    return render_template("resume-upload.html")

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@bp.route("/resume-process", methods=['POST', 'GET'])
def resumeProcess():
    """ Processing uploaded resume """
    print(app.config['UPLOAD_FOLDER'])
    if request.method == 'POST':
        file = request.files['File']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # save file to specified directory
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return "File saved successfully"
        else:
            return "Invalid File"
    else:
        return redirect('/resume-upload')

