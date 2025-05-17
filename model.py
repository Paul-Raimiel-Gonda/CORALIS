# model.py

import cv2
import numpy as np
import tensorflow as tf
from tensorflow import keras
from werkzeug.datastructures import FileStorage

# Load your pre-trained model once
model = keras.models.load_model('models/imageclassifier_three.keras')

def predict_coral_health(image_file: FileStorage):
    """
    Accepts an image file from the Flask API, processes it, and predicts coral health.
    Returns: "Healthy" or "Bleached"
    """
    try:
        # Convert to NumPy array
        file_bytes = np.frombuffer(image_file.read(), np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        # Resize and normalize image
        resize = tf.image.resize(img, (256, 256))
        normalized = np.expand_dims(resize / 255.0, 0)

        # Model prediction
        yhat = model.predict(normalized)

        # Logging for debugging (optional)
        print(f"Raw prediction: {yhat[0][0]}")

        return "Healthy Coral 🟢" if yhat[0][0] > 0.5 else "Bleached Coral ⚠️"

    except Exception as e:
        print("Prediction error:", e)
        return "Error in prediction"
