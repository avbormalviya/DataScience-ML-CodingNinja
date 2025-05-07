# Import necessary libraries
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler

# Load the Breast Cancer dataset from sklearn
data = load_breast_cancer()
x = data.data               # Features (30-dimensional)
y = data.target             # Target labels (0 = malignant, 1 = benign)

# Standardize the features (mean=0, std=1) to help model convergence
scaler = StandardScaler()
x = scaler.fit_transform(x)

# Split the dataset into training and testing sets (80% train, 20% test)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# Initialize logistic regression model with max_iter and saga solver
model = LogisticRegression(max_iter=1000, solver='saga')
model.fit(x_train, y_train)         # Train the model on the training data

# Print model parameters (like C, penalty, etc.)
print(model.get_params())

# Evaluate and print accuracy on both training and testing sets
print(model.score(x_train, y_train))   # Training accuracy
print(model.score(x_test, y_test))     # Testing accuracy

# Print the predicted probabilities for both training and testing data
# Each row contains [probability of class 0, probability of class 1]
print(model.predict_proba(x_train))
print(model.predict_proba(x_test))
