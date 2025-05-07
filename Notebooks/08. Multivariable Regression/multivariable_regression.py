import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Load CSV data: each row is a house, columns are features (e.g., rooms, age, etc.)
# Last column is the target (e.g., house price)
data = np.loadtxt('Boston.csv', delimiter=',', skiprows=1)

# Split the data into input features (X) and target values (y)
X = data[:, :-1]  # All columns except the last
y = data[:, -1]   # Only the last column

# Optional: normalize the data to improve model performance (important for multivariate)
# X = (X - np.mean(X, axis=0)) / np.std(X, axis=0)

# Split the data into training and testing sets (70% train, 30% test)
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.3, random_state=42)


# Train the linear regression model: calculate slope (m) and intercept (c)
def fit(x_train, y_train):
    m = []  # List to store slopes for each feature
    n_features = x_train.shape[1]  # Number of input columns/features

    # Loop through each feature/column
    for i in range(n_features):
        col = x_train[:, i]              # One feature column
        x_mean = np.mean(col)            # Mean of that feature
        y_mean = np.mean(y_train)        # Mean of target

        # Compute slope using least squares formula
        numerator = np.sum((col - x_mean) * (y_train - y_mean))
        denominator = np.sum((col - x_mean) ** 2)

        m.append(numerator / denominator)  # Append the slope for this feature

    # Calculate intercept (c) using the formula:
    # c = ȳ - m1*x̄1 - m2*x̄2 - ... - mn*x̄n
    y_mean = np.mean(y_train)
    x_means = np.mean(x_train, axis=0)
    c = y_mean - np.dot(m, x_means)

    return np.array(m), c  # Convert slopes to numpy array


# Predict outputs using the learned weights
def predict(x, m, c):
    return np.dot(x, m) + c  # Dot product: m1*x1 + m2*x2 + ... + c


# Evaluate model performance using R^2 score
def score(y_truth, y_pred):
    u = ((y_truth - y_pred) ** 2).sum()             # Residual sum of squares
    v = ((y_truth - y_truth.mean()) ** 2).sum()     # Total sum of squares
    return 1 - u / v                                # R^2 = 1 - (residual / total)


# Cost function = Mean Squared Error (MSE)
def cost(x, y, m, c):
    y_pred = predict(x, m, c)
    return np.mean((y - y_pred) ** 2)  # Average squared error


# Train the model
m, c = fit(X_train, Y_train)

# Make predictions on both train and test data
y_test_pred = predict(X_test, m, c)
y_train_pred = predict(X_train, m, c)

# Print R^2 scores and training cost
print("Test Score (R^2):", round(score(Y_test, y_test_pred), 2))
print("Train Score (R^2):", round(score(Y_train, y_train_pred), 2))
print("Training Cost (MSE):", round(cost(X_train, Y_train, m, c), 2))


# --- Visualize Actual vs Predicted (Test Data) ---
plt.figure(figsize=(8, 6))
plt.scatter(Y_test, y_test_pred, color='blue', alpha=0.6, label="Predicted vs Actual")
plt.plot([Y_test.min(), Y_test.max()], [Y_test.min(), Y_test.max()], color='red', linestyle='--', label="Ideal Prediction")
plt.xlabel("Actual House Prices")
plt.ylabel("Predicted House Prices")
plt.title("Actual vs Predicted (Test Set)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
