import os
import json
from PIL import Image
import numpy as np
import tensorflow as tf
import streamlit as st

from utils.download_model import download_model_from_drive

# Paths
working_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(working_dir, "trained_model", "plant_disease_prediction_model.h5")
class_indices_path = os.path.join(working_dir, "class_indices.json")

# Download model if not exists
download_model_from_drive(file_id="1wdhbZ9PkpL0ok3IciUGX2ElaaYtQyXcu", output_path=model_path)

# Load the model
model = tf.keras.models.load_model(model_path)

# Load class indices
with open(class_indices_path, 'r') as f:
    class_indices = json.load(f)


# Image preprocessing
def load_and_preprocess_image(image, target_size=(224, 224)):
    img = image.resize(target_size)
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array.astype('float32') / 255.0
    return img_array


# Predict class
def predict_image_class(model, image, class_indices):
    processed_img = load_and_preprocess_image(image)
    predictions = model.predict(processed_img)
    predicted_index = np.argmax(predictions, axis=1)[0]
    return class_indices[str(predicted_index)]


# Streamlit App
st.title("🌿 Plant Disease Classifier")

uploaded_image = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    col1, col2 = st.columns(2)

    with col1:
        st.image(image.resize((200, 200)), caption="Uploaded Image")

    with col2:
        if st.button("Classify"):
            prediction = predict_image_class(model, image, class_indices)
            st.success(f"Prediction: {prediction}")