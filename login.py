from flask import Blueprint, request, Flask, render_template, redirect
from flask_login import current_user, login_user, logout_user

bp = Blueprint("login", __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    """ Login as owner """
    if request.method == 'POST':
        user = request.form['user-name']
        password = request.form['user-password']
        return password
    return render_template('login.html')

@bp.route('/logout')
def logout():
    """ Logout as owner """
    return "Logout"