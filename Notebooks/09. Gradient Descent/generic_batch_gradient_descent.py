import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# --- Load and Prepare Data ---
# Load dataset (skip the header row), split features and target
fuelEconomy = np.loadtxt("Boston.csv", delimiter=",", skiprows=1)
X = fuelEconomy[:, :-1]  # All columns except last = features
Y = fuelEconomy[:, -1]   # Last column = target

# Split dataset into training and testing sets (80% train, 20% test)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)


# --- Batch Gradient Descent Step ---
def step(x, y, m, c, learning_rate):
    m_grad = np.zeros(len(m))  # Initialize slope gradients for all features
    c_grad = 0                 # Initialize intercept gradient

    for i in range(len(x)):
        y_pred_i = np.dot(x[i], m) + c       # Prediction for x[i]
        error = y[i] - y_pred_i              # Error for that prediction

        # Accumulate gradients
        m_grad += (-2 / len(x)) * error * x[i]  # Vector update for slopes
        c_grad += (-2 / len(x)) * error         # Scalar update for intercept

    # Update parameters
    m = m - learning_rate * m_grad
    c = c - learning_rate * c_grad

    return m, c


# --- Batch Gradient Descent Runner ---
def gradient_descent(x, y, learning_rate, iterations):
    m = np.zeros(x.shape[1])  # Initialize weights (one per feature)
    c = 0                     # Initialize bias

    for i in range(iterations):
        m, c = step(x, y, m, c, learning_rate)
        print(f"Iteration {i+1}, Cost: {cost(x, y, m, c)}")  # Track loss

    return m, c


# --- Mean Squared Error (Cost Function) ---
def cost(x, y, m, c):
    return np.mean((y - (np.dot(x, m) + c)) ** 2)


# --- Prediction Function ---
def predict(x, m, c):
    return np.dot(x, m) + c


# --- R² Score (Performance Metric) ---
def score(y_truth, y_pred):
    u = ((y_truth - y_pred) ** 2).sum()  # Residual sum of squares
    v = ((y_truth - y_truth.mean()) ** 2).sum()  # Total sum of squares
    return 1 - u / v  # R² = 1 - (residual / total)


# --- Train the Model ---
m, c = gradient_descent(X_train, Y_train, learning_rate=0.000001, iterations=100)

# --- Make Predictions ---
Y_pred = predict(X_test, m, c)

# --- Evaluate Performance ---
print("R² Score:", score(Y_test, Y_pred))


# --- Visualize Actual vs Predicted ---
plt.figure(figsize=(8, 6))
plt.scatter(Y_test, Y_pred, color='blue', alpha=0.6, label="Predicted vs Actual")
plt.plot([Y_test.min(), Y_test.max()], [Y_test.min(), Y_test.max()], color='red', linestyle='--', label="Ideal Prediction")
plt.xlabel("Actual House Prices")
plt.ylabel("Predicted House Prices")
plt.title("Actual vs Predicted (Test Set)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
