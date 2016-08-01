import os

from werkzeug.utils import secure_filename

__author__ = 'tharinda'

# import classes
from uicontroller.Main import *
from core.packages.pdf_reader.PDF_Reader import *
from core.dbmgt.usermgt.user import User
# import libraries
from flask import *
from flask_restful import Api

app = Flask(__name__)
app.config.from_object(__name__)
api = Api(app)

api.add_resource(Main, '/', endpoint='/')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


# Route that will process the file upload
@app.route('/upload', methods=['POST'])
def upload():
    # Get the name of the uploaded file
    file = request.files['file']
    # Check if the file is one of the allowed types/extensions
    if file and allowed_file(file.filename):
        # Make the filename safe, remove unsupported chars
        filename = secure_filename(file.filename)
        # Move the file form the temporal folder to
        # the upload folder we setup
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Redirect the user to the uploaded_file route, which
        # will basicaly show on the browser the uploaded file
        User = CV_reader(filename)
        if User == "Wrong Template":
            return "Wrong Template"
        # return redirect(url_for('uploaded_file',
        #                         filename=filename))

        # print extractor.extract(txt)
        return json.dumps(User.__dict__)


# This route is expecting a parameter containing the name
# of a file. Then it will locate that file on the upload
# directory and show it on the browser, so if the user uploads
# an image, that image is going to be show after the upload
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
