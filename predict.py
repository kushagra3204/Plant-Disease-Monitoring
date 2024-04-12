from keras.preprocessing.image import load_img, img_to_array, ImageDataGenerator
from keras.models import load_model
import tensorflow as tf
import numpy as np
import sys
import os

def preprocess_img(img_path,target_size=(255,255)):
    img = load_img(img_path,target_size=target_size)
    x = img_to_array(img)
    x = x.astype('float32')/255
    x = np.expand_dims(x,axis=0)
    return x

x = preprocess_img('test1.png')

train_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)

train_generator = train_datagen.flow_from_directory(
    'data/train',
    target_size=(255,255),
    batch_size=32,
    class_mode='categorical'
)

model = load_model('model/WDDModel.h5')
prediction = model.predict(x)
labels = train_generator.class_indices
labels = {v: k for k,v in labels.items()}

predicted_class = labels[np.argmax(prediction)]
print(predicted_class)