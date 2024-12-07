from keras.preprocessing.image import load_img, img_to_array
import numpy as np
import tensorflow as tf

def preprocess_img(img_path, target_size=(255, 255)):
    img = load_img(img_path, target_size=target_size)
    x = img_to_array(img)
    x = x.astype('float32') / 255
    x = np.expand_dims(x, axis=0)
    return x

def classify_image(img_path):
    x = preprocess_img(img_path)
    tflite_model_path = './model/model_new.tflite'
    interpreter = tf.lite.Interpreter(model_path=tflite_model_path)
    interpreter.allocate_tensors()
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    interpreter.set_tensor(input_details[0]['index'], x)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])
    labels = {
        0: 'Aphid', 1: 'Black Rust', 2: 'Blast', 3: 'Brown Rust', 4: 'Common Root Rot',
        5: 'Fusarium Head Blight', 6: 'Healthy', 7: 'Leaf Blight', 8: 'Mildew', 9: 'Mite',
        10: 'Septoria', 11: 'Smut', 12: 'Stem fly', 13: 'Tan spot', 14: 'Yellow Rust'
    }
    predicted_class = labels[np.argmax(output_data)]
    return predicted_class