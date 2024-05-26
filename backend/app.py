from werkzeug.utils import secure_filename
from predict import classify_image
from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/predict', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'fileReceived': False, 'disease': None})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'fileReceived': False, 'disease': None})

    filename = secure_filename(file.filename)
    saved_img_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(saved_img_path)

    try:
        class_predicted = classify_image(saved_img_path)
    finally:
        os.remove(saved_img_path)

    return jsonify({'fileReceived': True, 'disease': class_predicted})

if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=5000, threads=1, connection_limit=1000, channel_timeout=1200)