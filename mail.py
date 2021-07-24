from flask import Blueprint, request, Flask, render_template, redirect 
from flask_mail import Mail, Message
from app import mail, app
import flask

bp = Blueprint("mail", __name__)

@bp.route("/mail/", methods= ['POST'])
def send_mail():
    """ Route for sending mail """
    try: 
        if request.method == "POST":
            email = request.form['sent-email']
            password = request.form['sent-password']
            subject = request.form['sent-subject']
            message = request.form['sent-message']

            app.config.update (
                MAIL_USERNAME = email,
                MAIL_PASSWORD = password
            )

            msg = Message(
                subject,
                sender=email,
                recipients=["hilfus20@gmail.com"])
            msg.body = message
            mail.send(msg)
            return "Sent mail!"
    except Exception as e:
        return render_template('index.html', mail_error = (str(e)))


