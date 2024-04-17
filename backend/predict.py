from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
import numpy as np

def preprocess_img(img_path, target_size=(255, 255)):
    img = load_img(img_path, target_size=target_size)
    x = img_to_array(img)
    x = x.astype('float32') / 255
    x = np.expand_dims(x, axis=0)
    return x

def classify_image(img_path):
    x = preprocess_img(img_path)
    model = load_model('model/WDDModel.h5')
    prediction = model.predict(x)
    labels = {
        0: 'Aphid', 1: 'Black Rust', 2: 'Blast', 3: 'Brown Rust', 4: 'Common Root Rot',
        5: 'Fusarium Head Blight', 6: 'Healthy', 7: 'Leaf Blight', 8: 'Mildew', 9: 'Mite',
        10: 'Septoria', 11: 'Smut', 12: 'Stem fly', 13: 'Tan spot', 14: 'Yellow Rust'
    }
    predicted_class = labels[np.argmax(prediction)]
    return predicted_class