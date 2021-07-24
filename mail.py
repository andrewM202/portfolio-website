from flask import Blueprint, request, Flask, render_template, redirect 
from flask_mail import Mail, Message
from app import mail
import flask

bp = Blueprint("mail", __name__)

@bp.route("/mail/", methods= ['POST'])
def send_mail():
    """ Route for sending mail """
    try: 
        if request.method == "POST":
            email = request.form['sent-email']
            name = request.form['sent-name']
            subject = request.form['sent-subject']
            message = request.form['sent-message']

            #from app import app, Config
            from app import app

            print(app.config)

            msg = Message(
                subject,
                sender=email,
                recipients=["hilfus20@gmail.com"])
            msg.body = "Message from " + name + ", email: " + email + "\n\n" + message
            mail.send(msg)
            return render_template('index.html', mail_success="Email Successfully Sent!")
    except Exception as e:
        #print(e)
        return render_template('index.html', mail_error=(str(e)))


