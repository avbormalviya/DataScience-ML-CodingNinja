import pandas as pd
import numpy as np
from collections import defaultdict
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Fit function to create the Naive Bayes model from scratch
def fit(x_train, y_train):
    summary = defaultdict(dict)  # Use defaultdict to automatically initialize keys

    x_train = pd.DataFrame(x_train)  # Convert training data into a DataFrame
    y_train = pd.Series(y_train)  # Convert target into a Series

    for curr_class in y_train.unique():  # Loop through each unique class
        curr_class_df = x_train[y_train == curr_class]  # Filter data for each class

        for feature in x_train.columns:  # Loop through each feature (column)
            summary[curr_class][feature] = curr_class_df[feature].value_counts().to_dict()  # Count value occurrences

        summary[curr_class]['total'] = len(curr_class_df)  # Store the number of samples for each class

    summary['total'] = len(x_train)  # Store the total number of samples

    return summary

# Calculate the probability for each class given the test data and using Laplace Smoothing
def probability(summary, curr_class, x_test, alpha=2):
    output = np.log(summary[curr_class]['total']) - np.log(summary['total'])  # Log of prior probability

    num_features = len(summary[curr_class].keys()) - 1  # Subtract 1 to exclude 'total'

    for i in range(num_features):  # Loop over each feature
        feature = col_names[i]  # Get the feature name from column names
        value = x_test[i]  # Get the value of the feature in the test data

        # Laplace Smoothing for unseen values
        count = summary[curr_class][feature].get(value, 0)  # Get the count for the feature value (0 if not found)
        total = summary[curr_class]['total']  # Total samples for the class
        k = len(summary[curr_class][feature])  # Number of unique values for the feature
        prob = np.log(count + alpha) - np.log(total + alpha * k)  # Smoothing formula

        output += prob  # Add the feature'scratch_KNN.py probability to the overall class probability

    return output

# Predict the class for a single test instance
def predictSingle(summary, x_test):
    max_prob = -1  # Initialize max probability with a very low number
    best_class = None  # Initialize best class as None

    first_time = True  # Flag to check if it'scratch_KNN.py the first iteration

    for curr_class in summary.keys():  # Loop through each class
        if curr_class == 'total':  # Skip the total key
            continue

        curr_prob = probability(summary, curr_class, x_test)  # Calculate probability for current class

        if first_time or curr_prob > max_prob:  # If it'scratch_KNN.py the first class or has the highest probability
            max_prob = curr_prob  # Update the max probability
            best_class = curr_class  # Update the best class
            first_time = False  # Set flag to False after the first iteration

    return best_class  # Return the predicted class

# Function to predict all the classes for the test set
def predict(summary, x_test):
    predictions = []  # List to store predictions

    for x in x_test:  # Loop through each test instance
        predictions.append(predictSingle(summary, x))  # Get the predicted class for each instance

    return predictions  # Return the list of predictions

# Column names for the dataset
col_names = ['sl', 'sw', 'pl', 'pw', 'flower_type']
labels = ["low", "medium", "high"]  # Categories to discretize continuous features

# Load the Iris dataset from sklearn
iris = load_iris()

# Convert the dataset into a DataFrame and map target labels
df = pd.DataFrame(data=iris.data, columns=col_names[:-1])  # DataFrame for features
df['flower_type'] = iris.target  # Add target column
df['flower_type'] = df['flower_type'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})  # Map target to class names

# Discretize the features into the 'low', 'medium', 'high' categories
for col in df.columns[:-1]:  # Loop through each feature column (except the target column)
    df[col] = pd.cut(df[col], bins=len(labels), labels=labels)  # Use pd.cut to discretize the data

# Split the data into training and testing sets (80% train, 20% test)
x_train, x_test, y_train, y_test = train_test_split(df[col_names], df['flower_type'], test_size=0.2, random_state=42)

# Fit the model with training data
summary = fit(x_train, y_train)

# Predict the classes for the test set
y_pred = predict(summary, x_test.values)

# Evaluate the model using accuracy, classification report, and confusion matrix
print(accuracy_score(y_test, y_pred))  # Accuracy of the model
print(classification_report(y_test, y_pred))  # Detailed classification metrics
print(confusion_matrix(y_test, y_pred))  # Confusion matrix showing performance
