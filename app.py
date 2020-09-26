#----------------------------Main - Chat App----------------------------------#
# Author:       Magister17
# Version:      v1.0#
# GitHub URL:   https://github.com/Magister17/chat-app-17
#-----------------------------------------------------------------------------#

# import section
import os
import time
from flask import Flask, render_template
#from flask import Flask, render_template, request, redirect, url_for, flash
from flask_socketio import SocketIO #, join_room, leave_room, send


app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)