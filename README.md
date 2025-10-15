Iris Flower Species Prediction App

This project is a web-based machine learning application built with Streamlit. It predicts the species of an Iris flower based on four input features: sepal length, sepal width, petal length, and petal width. The model powering this application is a Random Forest Classifier trained on the Iris dataset provided by the `scikit-learn` library.


Application

Access the deployed application here:  
[Iris Flower Species Prediction App](https://iris-flask-app-q2cfgk5vyscj2jjpgsjvhk.streamlit.app/)


Project Overview

The Iris dataset is a well-known classification dataset commonly used to demonstrate supervised learning algorithms.  
This application provides an interactive interface that allows users to adjust the flower’s measurements using sliders and instantly view the predicted species.

Key Features:
- Interactive input sliders for sepal and petal measurements  
- Real-time species prediction output  
- Data visualization showing feature distributions  
- Model information and performance details  

Model Summary:
- Algorithm: Random Forest Classifier  
- Accuracy: Approximately 97.8%  
- Features: Sepal Length, Sepal Width, Petal Length, Petal Width  
- Libraries Used: `scikit-learn`, `pandas`, `numpy`, `streamlit`

Running the Application Locally

Follow these steps to run the Streamlit app on your local machine:

1. Clone the repository
   ```bash
   git clone https://github.com/Willflores1/iris-flask-app.git
   cd iris-flask-app

2. Create and activate a virtual environment
    python -m venv .venv
    # On Windows
    .venv\Scripts\activate
    # On macOS/Linux
    source .venv/bin/activate

3. Install the required dependencies
    pip install -r requirements.txt

4. Run the Streamlit application
    streamlit run streamlitapp.py

5. View the app in your browser
    http://localhost:8501

Repository Structure
├── streamlitapp.py          # Main Streamlit application script
├── classifier.pkl           # Trained Random Forest model
├── requirements.txt         # List of dependencies
└── README.md                # Project documentation

Deployment

The application is deployed on Streamlit Cloud, which automatically installs dependencies, sets up the environment, and serves the app from the GitHub repository.
This enables real-time public access through a shareable URL.