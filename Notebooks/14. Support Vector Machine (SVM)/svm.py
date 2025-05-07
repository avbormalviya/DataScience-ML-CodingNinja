# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC

# Load the Iris dataset
iris = load_iris()

# Split the dataset into training and testing sets (80% train, 20% test)
x_train, x_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=42
)

# Create a Support Vector Classifier (SVC) model
svc = SVC()

# Define a clean hyperparameter grid
param_grid = [
    {'kernel': ['linear'], 'C': [0.01, 0.1, 1, 10, 100]},
    {'kernel': ['rbf'], 'C': [0.1, 1, 10], 'gamma': [0.01, 0.1, 1, 'scale', 'auto']}
]

# Setup GridSearchCV with 5-fold cross-validation
model = GridSearchCV(svc, param_grid, cv=5)

# Train the model using only the first two features (for 2D plotting)
model.fit(x_train[:, :2], y_train)

# Print best parameters found
print("Best Parameters:", model.best_params_)

# Print the model accuracy on test data
print("Test Accuracy:", model.score(x_test[:, :2], y_test))


# Function to create a mesh grid of points
def meshGrid(x1, x2, h=0.02):
    x1_min, x1_max = x1.min() - 1, x1.max() + 1
    x2_min, x2_max = x2.min() - 1, x2.max() + 1
    xx1, xx2 = np.meshgrid(
        np.arange(x1_min, x1_max, h),
        np.arange(x2_min, x2_max, h)
    )
    return xx1, xx2


# Generate a mesh grid based on training data
xx1, xx2 = meshGrid(x_train[:, 0], x_train[:, 1])

# Use the best estimator for prediction
best_model = model.best_estimator_
prediction = best_model.predict(np.c_[xx1.ravel(), xx2.ravel()])

# Scatter plot of the training data
plt.scatter(x_train[:, 0], x_train[:, 1], c=y_train, cmap='rainbow', edgecolor='k')

# Plot the decision boundary using contourf
plt.contourf(xx1, xx2, prediction.reshape(xx1.shape), alpha=0.3, cmap='rainbow')

plt.title('SVC Decision Boundary (After Grid Search)')
plt.show()
