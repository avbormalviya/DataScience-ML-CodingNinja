# Import required modules
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
X = iris.data           # Feature matrix
y = iris.target         # Target labels

# Split the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Initialize the MLP (Multi-layer Perceptron) classifier
mlp = MLPClassifier(
    hidden_layer_sizes=(10, 10, 10),  # Three hidden layers with 10 neurons each
    max_iter=1000,                    # Maximum number of training iterations
    alpha=0.0001,                     # L2 regularization term (to avoid overfitting)
    solver='adam',                   # Optimizer for weight optimization
    verbose=True,                    # Print progress during training
    random_state=42                  # Reproducibility
)

# Train the model on the training data
mlp.fit(X_train, y_train)

# Print the model's accuracy on the test data
print(f"Test Accuracy: {mlp.score(X_test, y_test):.2f}")
