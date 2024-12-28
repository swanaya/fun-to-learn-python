# Filename: flask_model_ui.py

from flask import Flask, request, render_template
import pickle
import numpy as np


app = Flask(__name__)

# Load the model (replace with your own model path)
model = pickle.load(open('linear_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            input_value = float(request.form['number'])
            prediction = model.predict(np.array([[input_value]]))[0]
            return render_template('index.html', prediction_text=f"Predicted value: {prediction}")
        except ValueError:
            return render_template('index.html', prediction_text="Please enter a valid number.")
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
