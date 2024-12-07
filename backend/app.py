from werkzeug.utils import secure_filename
from predict import classify_image
from flask import Flask, request, jsonify, render_template, make_response
from flask_cors import CORS
import os
import logging

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE

logging.basicConfig(level=logging.INFO)

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'bmp'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET'])
def main_page():
    return make_response("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Image Classification API</title>
    </head>
    <body>
        <h1>Welcome to the Image Classification API</h1>
        <p>Use the <code>/predict</code> endpoint to upload an image and classify it.</p>
    </body>
    </html>
    """, 200)

@app.route('/predict', methods=['POST'])
def upload():
    if 'file' not in request.files:
        logging.warning("No file part in the request")
        return jsonify({'fileReceived': False, 'error': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        logging.warning("Empty filename provided")
        return jsonify({'fileReceived': False, 'error': 'No selected file'})

    if not allowed_file(file.filename):
        logging.warning(f"Invalid file type: {file.filename}")
        return jsonify({'fileReceived': False, 'error': 'Invalid file type'})

    filename = secure_filename(file.filename)
    saved_img_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(saved_img_path)
    logging.info(f"File {filename} saved successfully")

    try:
        class_predicted = classify_image(saved_img_path)
        logging.info(f"Classification successful for {filename}")
    except Exception as e:
        logging.error(f"Error during classification: {str(e)}")
        return jsonify({'fileReceived': True, 'error': 'Classification failed'})
    finally:
        os.remove(saved_img_path)
        logging.info(f"File {filename} removed after processing")

    return jsonify({'fileReceived': True, 'disease': class_predicted})

@app.errorhandler(404)
def page_not_found(e):
    return make_response("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>404 - Page Not Found</title>
    </head>
    <body>
        <h1>404 - Page Not Found</h1>
        <p>The page you are looking for does not exist. Please check the URL.</p>
    </body>
    </html>
    """, 404)

if __name__ == '__main__':
    from waitress import serve
    logging.info("Starting server...")
    serve(app, host='0.0.0.0', port=5000, threads=4, connection_limit=1000, channel_timeout=1200)