from flask import Blueprint, request, Flask, render_template, redirect, jsonify
from flask_login import current_user, login_user, logout_user
from models import User

bp = Blueprint("login", __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    """ Login as owner """
    if current_user.is_authenticated:
        return render_template("login.html")
    elif request.method == 'POST':
        username = request.form['user-name']
        password = request.form['user-password']
        if username is not None and password is not None:
            db_user = User.objects().first().username
            db_pass = User.objects().first().password
            if username == db_user and password == db_pass:
                loggedin_user = User.objects().first()
                login_user(loggedin_user)
                return render_template("login.html")
            else:
                return render_template('login.html')
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')

@bp.route('/logout', methods=['POST'])
def logout():
    """ Logout as owner """
    logout_user()
    return render_template("login.html")