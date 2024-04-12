from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential

# Data Augmentation on train dataset
train_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)

# Data Augmentation on test dataset
test_datagen = ImageDataGenerator(
    rescale=1./255
)

train_generator = train_datagen.flow_from_directory(
    'data/train',
    target_size=(255,255),
    batch_size=32,
    class_mode='categorical'
)

valid_generator = test_datagen.flow_from_directory(
    'data/valid',
    target_size=(255,255),
    batch_size=32,
    class_mode='categorical'
)

model = Sequential()
model.add(Conv2D(32,(3,3),input_shape=(255,255,3),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(64,(3,3),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Flatten())
model.add(Dense(64,activation='relu'))
model.add(Dense(15,activation='softmax'))

model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])
model.summary()

history = model.fit(
        train_generator,
        batch_size=32,
        epochs=100,
        validation_data=valid_generator,
        validation_batch_size=32,
)

model.save('WDDModel.h5')