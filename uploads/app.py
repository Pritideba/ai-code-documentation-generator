import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import os

# Get project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Correct model path
MODEL_PATH = os.path.join(BASE_DIR, "model", "land_classifier_model.keras")

# Load model
model = tf.keras.models.load_model(MODEL_PATH)

class_names = [
'AnnualCrop','Forest','HerbaceousVegetation','Highway',
'Industrial','Pasture','PermanentCrop','Residential',
'River','SeaLake'
]

st.title("AI Remote Sensing Land Classification")

st.write("Upload a satellite image")

# Show training graph
st.subheader("Model Training Performance")

if os.path.exists("../results/training_graph.png"):
    st.image("../results/training_graph.png")

uploaded_file = st.file_uploader(
    "Choose an image...", type=["jpg","png","jpeg"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Resize image
    img = image.resize((128,128))

    img_array = np.array(img)/255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)

    predicted_class = class_names[np.argmax(prediction)]
    confidence = np.max(prediction)*100

    st.success(f"Predicted Land Type: {predicted_class}")
    st.write(f"Confidence: {confidence:.2f}%")

    # Top 3 predictions
    st.subheader("Top 3 Predictions")

    top3_idx = prediction[0].argsort()[-3:][::-1]

    for i in top3_idx:
        st.write(f"{class_names[i]} : {prediction[0][i]*100:.2f}%")