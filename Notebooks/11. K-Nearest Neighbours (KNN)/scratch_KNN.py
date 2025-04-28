from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import accuracy_score
import numpy as np

# Load the breast cancer dataset from sklearn
cancer = load_breast_cancer()

# Split the dataset into training and testing sets (80-20 split)
x_train, x_test, y_train, y_test = train_test_split(cancer.data, cancer.target, random_state=42)


# Function to compute the Euclidean distance between two points (x1 and x2)
def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))  # Return the square root of the sum of squared differences


# Function to predict the label for a single test point
def predict_row(x_train, y_train, x, k):
    distances = []

    # Calculate the distance between the test point (x) and all points in the training set
    for i in range(len(x_train)):
        distances.append((i, euclidean_distance(x_train[i, :], x)))

    # Sort the distances in ascending order to find the closest neighbors
    distances.sort(key=lambda x: x[1])

    # Select the k nearest neighbors
    neighbors = distances[:k]

    # Get the labels of the nearest neighbors
    neighbors = [y_train[neighbors[i][0]] for i in range(len(neighbors))]

    # Return the most common label among the neighbors
    return Counter(neighbors).most_common(1)[0][0]


# Function to predict the labels for all test points
def predict(x_train, y_train, x_test, k):
    predictions = []

    # For each test point, predict its label using the k-NN algorithm
    for x in x_test:
        predictions.append(predict_row(x_train, y_train, x, k))

    return predictions


# Predict the labels for the test set using k=7
predictions = predict(x_train, y_train, x_test, 5)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, predictions)

# Print the accuracy of the k-NN model
print(accuracy)
