# !/usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask, render_template
from flask_socketio import SocketIO
from apscheduler.schedulers.background import BackgroundScheduler
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('realtime-data-view.html')


@socketio.on('connect')
def handle_connect():
    socketio.emit('server_response', 'success!')


@socketio.on('my event')
def handle_custom_event(json):
    print("received custom event from client: " + str(json))
    # while True:
    socketio.sleep(3)
    t = load_realtime_data()
    print("send message: " + t)
    socketio.emit('server_response', t)


def load_realtime_data():
    return "{data : generate_realtime_data_from_yuanyaru" + str(random.randint(0, 10)) + "}"


def generate_and_send_message():
    data = load_realtime_data()
    socketio.emit('server_response', data)


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(generate_and_send_message, 'interval', seconds=2)
    scheduler.start()
    socketio.run(app, debug=True)

