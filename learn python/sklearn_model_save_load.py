# Filename: sklearn_model_save_load.py

import pickle
from sklearn.linear_model import LinearRegression
import numpy as np

# Sample data
X = np.array([[1], [3], [5], [7], [9]])  # Features
y = np.array([10, 30, 50, 70, 90])       # Labels

# Initialize and train a simple linear regression model
model = LinearRegression()
model.fit(X, y)

# Save the trained model to a .pkl file
with open('linear_model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

print("Model saved to linear_model.pkl")

# Loading the model for later use
with open('linear_model.pkl', 'rb') as model_file:
    loaded_model = pickle.load(model_file)

# Test the model with new data
test_data = np.array([[11], [13], [15]])  # Example test inputs
predictions = loaded_model.predict(test_data)

print("Predictions for new data:", predictions)
