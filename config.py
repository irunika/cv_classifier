__author__ = 'tharinda'

# import libraries
import os
from flask import json
from controller import *

app.secret_key = os.urandom(24)
app.debug = True
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

BASE_DIR = os.path.dirname(os.path.dirname(__file__)) #os.path.dirname(os.path.dirname(__file__)
PathToUpload = BASE_DIR + "/cv_classifier/uploads/"