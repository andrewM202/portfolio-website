from flask import Blueprint, request, Flask, render_template, redirect
from flask_socketio import SocketIO, send, emit
from app import socketio
from sqlalchemy import text, create_engine

bp = Blueprint("quickchat", __name__)

@bp.route("/send", methods=['POST', 'GET'])
def send_message():
    """ Route for sending quickchat messages """



@socketio.on("load_messages")
def load_messages():
    """ Load last N messages """



@socketio.on("delete_message")
def delete_message():
    """ Delete a message """
