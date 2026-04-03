import streamlit as st
import tensorflow as tf
import numpy as np

# Load model
model = tf.keras.models.load_model("model.keras")

st.title("My ML App")

# Example input (modify based on your model)
input_value = st.number_input("Enter a value")

if st.button("Predict"):
    # Convert input into model format
    input_array = np.array([[input_value]])

    prediction = model.predict(input_array)

    st.write("Prediction:", prediction)