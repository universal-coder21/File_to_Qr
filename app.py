# from flask import Flask, render_template, request, redirect, url_for
# import os
# import uuid

# app = Flask(__name__)

# # Path to store uploaded files
# UPLOAD_FOLDER = 'static/uploads/'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # Ensure the upload directory exists
# if not os.path.exists(UPLOAD_FOLDER):
#     os.makedirs(UPLOAD_FOLDER)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     if 'file' not in request.files:
#         return 'No file part'
#     file = request.files['file']
#     if not file or not file.filename:
#         return 'No selected file'

#     # Ensure filename is a valid string
#     filename = str(uuid.uuid4()) + "_" + (file.filename or "")

#     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

#     # Generate the file link
#     file_url = url_for('static', filename='uploads/' + filename, _external=True)

#     return render_template('index.html', file_url=file_url)

# # if __name__ == '__main__':
# #     app.run(debug=True)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=8080)

# main.py
from flask import Flask, render_template, request, redirect, url_for
import os
import uuid

app = Flask(__name__)

# Path to store uploaded files
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'

    # Save file with a unique filename
    filename = str(uuid.uuid4()) + "_" + (file.filename or "")
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    # Generate the file link
    file_url = url_for('static', filename='uploads/' + filename, _external=True)

    # Redirect to QR code generation page
    return redirect(url_for('generate_qr', file_url=file_url))

@app.route('/generate_qr')
def generate_qr():
    # Pass the file URL to the QR code generator page
    file_url = request.args.get('file_url')
    return render_template('generate_qr.html', file_url=file_url)

