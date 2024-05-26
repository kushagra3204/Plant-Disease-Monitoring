from werkzeug.utils import secure_filename
from predict import classify_image
from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/predict',methods=['POST'])
def upload():

    if 'file' not in request.files:
        return {
            'fileRecieved': False,
            'disease': None
        }
    
    file = request.files['file']
    
    if file.filename == '':
        return {
            'fileRecieved': False,
            'disease': None
        }
    
    saved_img_path = 'uploads/'+secure_filename(file.filename)
    file.save(saved_img_path)
    
    class_predicted = classify_image(saved_img_path)
    
    os.remove(saved_img_path)
    
    return {
        'fileRecieved': True,
        'disease': class_predicted
    }


if __name__ == '__main__':
    app.run(debug=True)