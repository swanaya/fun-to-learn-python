# Filename: pytorch_model_save_load.py

import torch
import torch.nn as nn
import torch.optim as optim

# Define a simple linear regression model
class LinearModel(nn.Module):
    def __init__(self):
        super(LinearModel, self).__init__()
        self.linear = nn.Linear(1, 1)

    def forward(self, x):
        return self.linear(x)

# Initialize the model, loss function, and optimizer
model = LinearModel()
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Dummy data
X = torch.tensor([[1.0], [2.0], [3.0], [4.0], [5.0]])
y = torch.tensor([[2.0], [4.0], [6.0], [8.0], [10.0]])

# Train the model (just for demonstration)
for epoch in range(100):
    optimizer.zero_grad()
    outputs = model(X)
    loss = criterion(outputs, y)
    loss.backward()
    optimizer.step()

# Save the model in a .pth file
torch.save(model.state_dict(), "linear_model.pth")
print("Model saved as linear_model.pth")

# Loading the model for later use
loaded_model = LinearModel()
loaded_model.load_state_dict(torch.load("linear_model.pth"))
loaded_model.eval()  # Set the model to evaluation mode

# Test the model with new data
test_data = torch.tensor([[6.0], [7.0], [8.0]])
predictions = loaded_model(test_data)

print("Predictions for new data:", predictions)
