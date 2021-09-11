from flask import Blueprint, request, Flask, render_template, redirect, jsonify
from flask_socketio import SocketIO, send, emit
from models import Quickchat, db
from flask_mongoengine import MongoEngine
from datetime import datetime

bp = Blueprint("homepage", __name__)

@bp.route("/")
def query_all():
    """ Return all records for homepage """
    if len(Quickchat.objects()) > 0:
        messages = Quickchat.objects()
        length = len(messages)
        # return messages
        return render_template("index.html", messages=messages, length=length)
    else:
        return render_template("index.html")

@bp.route("/create_message", methods=["POST", "GET"])
def create_message():
    """ Test route for mongo engine """
    if request.method == "POST":
        message = request.form['user-message']
        name = request.form['user-name']

        user = Quickchat(
            name=name,
            message=message,
            datetime=datetime.now()
        )
        user.save()
    return redirect("/")

@bp.route("/query_test")
def query_test():
    """ Return all records """
    messages = Quickchat.objects()
    return jsonify(messages)

@bp.route("/query_record/<record>")
def query_record(record):
    """ Query records for mongo engine """
    user = Quickchat.objects(name=record).first()
    if not user:
        return jsonify({'error': 'data not found'}) 
    else:
        return jsonify(user.to_json())