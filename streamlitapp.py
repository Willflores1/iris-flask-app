# app.py

# 1. Imports
import streamlit as st
import numpy as np
import pickle
import pandas as pd
from sklearn.datasets import load_iris

# 2. Load Model
pickle_in = open("classifier.pkl", "rb")
classifier = pickle.load(pickle_in)

# 3. Page Setup
st.set_page_config(page_title="Iris Flower Classifier", page_icon="🌸", layout="centered")

# 4. Header / Description
st.title("🌸 Iris Flower Species Prediction App")
st.markdown("Predict the type of Iris flower using its measurements.")


# Component #1: Input Widgets (sliders)
st.subheader("Enter Flower Measurements:")
sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.1)
sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.5)
petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 1.4)
petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 0.2)

# Component #2: Button
if st.button("Predict"):
    # Model prediction
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = classifier.predict(features)[0]

    # Component #3: Display Output (Success message)
    st.success(f"The predicted Iris species is **{prediction}** 🌺")

# Component #4: Visualization (Chart)
st.subheader("📊 Feature Distribution Example")
iris = load_iris(as_frame=True)
st.bar_chart(iris.frame[['sepal length (cm)', 'petal length (cm)']].head(10))

# Component #5: Markdown/Info
st.markdown("""
---
### About the Model
This app uses a **Random Forest Classifier** trained on the Iris dataset.
- Accuracy: ~97.8%
- Features: Sepal & Petal length/width  
- Built with: `scikit-learn`, `pandas`, and `streamlit`
""")
