# Filename: sklearn_model_ui.py

import tkinter as tk
from tkinter import filedialog, messagebox
import pickle
import numpy as np

# Function to load the model
def load_model():
    global model
    file_path = filedialog.askopenfilename(filetypes=[("Pickle Files", "*.pkl")])
    if file_path:
        with open(file_path, 'rb') as model_file:
            model = pickle.load(model_file)
            messagebox.showinfo("Model Loaded", "The model has been successfully loaded!")
    else:
        messagebox.showwarning("No File Selected", "Please select a valid model file.")

# Function to make predictions
def predict():
    if model is None:
        messagebox.showwarning("No Model", "Please load a model first!")
        return

    try:
        input_value = float(entry.get())
        prediction = model.predict(np.array([[input_value]]))[0]
        result_label.config(text=f"Prediction: {prediction}")
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid number.")

# Initialize the main window
root = tk.Tk()
root.title("Model Prediction Interface")
root.geometry("400x200")

model = None  # Global variable for the model

# Create a label and entry for the input
input_label = tk.Label(root, text="Enter a number:")
input_label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

# Create buttons to load model and predict
load_button = tk.Button(root, text="Load Model", command=load_model)
load_button.pack(pady=10)

predict_button = tk.Button(root, text="Predict", command=predict)
predict_button.pack(pady=5)

# Create a label for the result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
