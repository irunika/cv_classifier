__author__ = 'tharinda'

# import classes
from uicontroller.Main import *

# import libraries
from flask import *
from flask_restful import Api

app = Flask(__name__)
app.config.from_object(__name__)
api = Api(app)

api.add_resource(Main, '/', endpoint='/')