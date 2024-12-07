import tensorflow as tf

# Step 1: Load your pre-trained Keras model
model_path = "model/WDDModel.h5"  # Ensure this path is correct and points to your model file
try:
    model = tf.keras.models.load_model(model_path)
    print("Model loaded successfully!")
except FileNotFoundError:
    print(f"Error: The file '{model_path}' does not exist.")
    exit()  # Exit the script if the model cannot be loaded

# Step 2: Convert the model to TFLite format
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]  # Optional: applies optimization to reduce size
tflite_model = converter.convert()

# Step 3: Save the TFLite model with a simple name
output_file_name = "model_new.tflite"  # Choose your desired file name
with open(output_file_name, 'wb') as f:
    f.write(tflite_model)

print(f"TFLite model conversion complete! Saved as '{output_file_name}'.")