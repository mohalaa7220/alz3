import os
import numpy as np
import requests
from io import BytesIO
from django.conf import settings
from tensorflow.keras.models import load_model
from PIL import Image, ImageOps


class ImageProcessor:
    """Handles image downloading, preprocessing, and transformation."""

    @staticmethod
    def preprocess_image(image_url):
        """Fetch and process the image from the given URL."""
        try:
            response = requests.get(image_url)
            response.raise_for_status()
            image = Image.open(BytesIO(response.content)).convert("RGB")
            image = ImageOps.fit(image, (224, 224), Image.Resampling.LANCZOS)
            image_array = np.asarray(image, dtype=np.float32)
            normalized_image = (image_array / 127.5) - 1
            return np.expand_dims(normalized_image, axis=0)
        except Exception:
            return None


class ModelHandler:
    """Manages model loading, caching, and prediction handling."""

    model = None
    class_names = None

    @classmethod
    def load_model_and_labels(cls):
        """Loads and caches the model and labels if not already loaded."""
        if cls.model is None:
            model_path = os.path.join(settings.BASE_DIR, 'keras_model.h5')
            cls.model = load_model(model_path, compile=False)
            cls.model.compile(optimizer='adam',
                              loss='sparse_categorical_crossentropy',
                              metrics=['accuracy'])

        if cls.class_names is None:
            labels_path = os.path.join(settings.BASE_DIR, 'labels.txt')
            with open(labels_path, "r") as file:
                cls.class_names = [line.strip() for line in file.readlines()]

    @classmethod
    def predict(cls, processed_image):
        """Runs the model prediction and returns severity level and confidence score."""
        cls.load_model_and_labels()
        prediction = cls.model.predict(processed_image)
        index = np.argmax(prediction)
        severity_level = cls.class_names[index].split()[-1]
        confidence_score = float(prediction[0][index])
        return severity_level, confidence_score
