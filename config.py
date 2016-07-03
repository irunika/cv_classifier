__author__ = 'tharinda'

# import libraries
import os
from flask import json
from controller import *

app.secret_key = os.urandom(24)
app.debug = True

BASE_DIR = os.path.dirname(os.path.dirname(__file__))