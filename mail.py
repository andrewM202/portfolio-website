from flask import Blueprint, request, Flask, render_template, redirect 
from flask_mail import Mail, Message
from app import mail, app
import flask

bp = Blueprint("mail", __name__)

@bp.route("/mail/")
def send_mail():
    """ Route for sending mail """
    try: 
        msg = Message(
            "Send mail test",
            sender="guardosilo@gmail.com",
            recipients=["hilfus20@gmail.com"])
        msg.body = "Hey!\nHow are you feeling?"
        mail.send(msg)
        return "Sent mail!"
    except Exception as e:
        return(str(e))


