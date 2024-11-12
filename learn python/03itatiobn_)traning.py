import random
from sklearn.linear_model import LinearRegression
import numpy as np

# Initialize variables
data = []
labels = []

# Loop to generate random data (simulating your numbers or strings)
for i in range(1, 100, 2):
    # Auto-picking a random number (simulating string/number picking)
    number = random.randint(1, 100)
    print(f"Picked number: {number}")
    
    # Store the number in data (you could store strings too)
    data.append([i])  # Using i as feature input
    labels.append(number)  # Number becomes the label (output we want to predict)

# Converting data to numpy arrays (required for scikit-learn)
X = np.array(data)  # Features
y = np.array(labels)  # Labels

# Initialize and train a simple linear regression model
model = LinearRegression()
model.fit(X, y)

# Test the model with some new data
test_data = np.array([[101], [103], [105]])  # Example test inputs (new "i" values)
predictions = model.predict(test_data)

print("Predictions for new data:", predictions)

# Save data to a file
with open("result.txt", "w", encoding="utf-8") as f:
    for i, pred in zip(test_data, predictions):
        f.write(f"i: {i[0]}, predicted value: {pred}\n")

# Optionally, pause before program ends
import time
time.sleep(5)
