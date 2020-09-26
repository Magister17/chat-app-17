#----------------------------Main - Chat App----------------------------------#
# Author:       Magister17
# Version:      v1.0
#
# GitHub URL:   https://github.com/Magister17/chat-app-17
#-----------------------------------------------------------------------------#

# import section
import os                       # utilizzata per interagire con sistema operativo
import time
from flask_socketio import SocketIO
from flask import Flask, render_template


app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)