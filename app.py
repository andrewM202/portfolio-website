from flask import Flask, render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

@app.route('/')
def hello_world():
    return render_template("index.html")


socketio = SocketIO(app)

if __name__ == "__main__":
    socketio.run(app)
