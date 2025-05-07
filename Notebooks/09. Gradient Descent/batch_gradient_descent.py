import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Load dataset
fuelEconomy = np.loadtxt("FuelEconomy.csv", delimiter=",")

# Separate into input feature (X) and target (Y)
X = fuelEconomy[:, 0].reshape(-1, 1)  # Feature column as 2D array
Y = fuelEconomy[:, 1]                 # Target column

# Split into training and testing sets (80% train, 20% test)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)


# --- Batch Gradient Descent Step Function ---
def step(x, y, m, c, learning_rate):
    m_grad = 0  # Gradient accumulator for slope
    c_grad = 0  # Gradient accumulator for intercept

    # Loop over each training sample
    for i in range(len(x)):
        y_pred = m * x[i] + c                # Prediction for x[i]
        error = y[i] - y_pred                # Error between actual and predicted

        # Accumulate gradients for m and c
        m_grad += (-2 / len(x)) * error * x[i]
        c_grad += (-2 / len(x)) * error

    # Update m and c using learning rate
    m = m - learning_rate * m_grad
    c = c - learning_rate * c_grad

    return m, c


# --- Batch Gradient Descent Loop ---
def gradient_descent(x, y, learning_rate, iterations):
    m = 0  # Initial slope
    c = 0  # Initial intercept

    for i in range(iterations):
        m, c = step(x, y, m, c, learning_rate)  # One update step
        print(f"Iteration {i+1}, Cost: {cost(x, y, m, c)}")  # Optional: track cost

    return m, c


# --- Mean Squared Error Cost Function ---
def cost(x, y, m, c):
    return np.mean((y - (m * x + c)) ** 2)


# --- Predict Function ---
def predict(x, m, c):
    return m * x + c


# --- R-squared Score Function ---
def score(y_truth, y_pred):
    u = ((y_truth - y_pred) ** 2).sum()  # Residual sum of squares
    v = ((y_truth - y_truth.mean()) ** 2).sum()  # Total sum of squares
    return 1 - u / v  # R² = 1 - (residual variance / total variance)


# --- Run Gradient Descent ---
m, c = gradient_descent(X_train, Y_train, learning_rate=0.00001, iterations=100)

# --- Make Predictions ---
Y_pred = predict(X_test, m, c)

# --- Evaluate Model ---
print("R² Score:", score(Y_test, Y_pred))


# --- Visualize Actual vs Predicted (Test Data) ---
plt.figure(figsize=(8, 6))
plt.scatter(Y_test, Y_pred, color='blue', alpha=0.6, label="Predicted vs Actual")
plt.plot([Y_test.min(), Y_test.max()], [Y_test.min(), Y_test.max()], color='red', linestyle='--', label="Ideal Prediction")
plt.xlabel("Actual Fuel Efficiency")
plt.ylabel("Predicted Fuel Efficiency")
plt.title("Actual vs Predicted (Test Set)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
