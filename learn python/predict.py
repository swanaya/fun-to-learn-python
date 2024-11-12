import pickle
import numpy as np

# Load the trained model from the .pkl file
with open('linear_model.pkl', 'rb') as model_file:
    loaded_model = pickle.load(model_file)

# Test the model with new data
test_data = np.array([[11], [13], [15]])  # Example test inputs
predictions = loaded_model.predict(test_data)

print("Predictions for new data:", predictions)
