from flask import Blueprint, request, Flask, render_template, redirect, jsonify
from flask_socketio import SocketIO, send, emit
from app import socketio
from models import Quickchat, db
from flask_mongoengine import MongoEngine
from datetime import datetime

bp = Blueprint("quickchat", __name__)

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

@bp.route("/query_all")
def query_all():
    """ Return all records """
    users = Quickchat.objects()
    return jsonify(users)

@bp.route("/query_record/<record>")
def query_record(record):
    """ Query records for mongo engine """
    user = Quickchat.objects(name=record).first()
    if not user:
        return jsonify({'error': 'data not found'}) 
    else:
        return jsonify(user.to_json())