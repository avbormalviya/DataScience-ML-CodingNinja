
# Problem statement

"""
Problem statement
For the given dataset "FuelEconomy.csv"

You need to write four functions namely:

1. fit(x_train, y_train)
2. predict(x, m, c)
3. score(y_truth, y_pred)
4. cost(x, y, m, c)

The output is going to print the training and testing score and the cost of the regressor
trained using the fit function.
"""


# Solution


import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Load CSV data: assumes two columns [feature, target]
data = np.loadtxt('FuelEconomy.csv', delimiter=',')

# Split data into input (X) and output (y)
X = data[:, 0]
y = data[:, 1]

# Split data into training and testing sets (70% train, 30% test)
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.3, random_state=42)


# Function to fit the linear regression model (calculate slope m and intercept c)
def fit(x_train, y_train):
    x_mean = np.mean(x_train)
    y_mean = np.mean(y_train)

    # Using formula: m = Σ[(x - x̄)(y - ȳ)] / Σ[(x - x̄)^2]
    numerator = np.sum((x_train - x_mean) * (y_train - y_mean))
    denominator = np.sum((x_train - x_mean) ** 2)

    m = numerator / denominator
    c = y_mean - m * x_mean
    return m, c


# Predict function using y = mx + c
def predict(x, m, c):
    return m * x + c


# R^2 score to evaluate model performance
def score(y_truth, y_pred):
    u = ((y_truth - y_pred) ** 2).sum()  # Residual sum of squares
    v = ((y_truth - y_truth.mean()) ** 2).sum()  # Total sum of squares
    return 1 - u / v  # R-squared formula


# Cost function: Mean Squared Error (MSE)
def cost(x, y, m, c):
    return ((y - (m * x + c)) ** 2).mean()


# Train the model
m, c = fit(X_train, Y_train)

# Predict using trained model
y_test_pred = predict(X_test, m, c)
y_train_pred = predict(X_train, m, c)

# Print R^2 scores and cost
print("Test Score (R^2):", round(score(Y_test, y_test_pred), 2))
print("Train Score (R^2):", round(score(Y_train, y_train_pred), 2))
print("Training Cost (MSE):", round(cost(X_train, Y_train, m, c), 2))


# 📈 Visualization section

plt.figure(figsize=(12, 5))

# Training data plot
plt.subplot(1, 2, 1)
plt.scatter(X_train, Y_train, color='blue', label='Training Data')
plt.plot(X_train, y_train_pred, color='red', label='Regression Line')
plt.title("Training Data Fit")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()

# Testing data plot
plt.subplot(1, 2, 2)
plt.scatter(X_test, Y_test, color='green', label='Testing Data')
plt.plot(X_test, y_test_pred, color='red', label='Regression Line')
plt.title("Testing Data Fit")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()

plt.tight_layout()
plt.show()
