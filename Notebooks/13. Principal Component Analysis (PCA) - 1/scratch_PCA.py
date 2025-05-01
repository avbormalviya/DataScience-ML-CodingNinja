import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the Breast Cancer dataset
cancer = load_breast_cancer()

# Standardize the data (mean = 0, std = 1)
scaler = StandardScaler()
cancer.data = scaler.fit_transform(cancer.data)

# Split the dataset into training and test sets
x_train, x_test, y_train, y_test = train_test_split(cancer.data, cancer.target, random_state=42)

# Calculate the covariance matrix of the training data (transpose needed to align features as rows)
cov_matrix = np.cov(x_train.T)

# Compute eigenvalues and eigenvectors of the covariance matrix
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

# Combine eigenvalues and corresponding eigenvectors into pairs
eigen_value_vector_pair = zip(eigenvalues, eigenvectors)

# Sort the eigenvalue-vector pairs in descending order of eigenvalue (importance)
eigen_value_vector_pair = sorted(eigen_value_vector_pair, key=lambda x: x[0], reverse=True)

# Display top 5 principal components (eigenvalues and partial eigenvectors)
for i, (val, vec) in enumerate(eigen_value_vector_pair[:5]):
    print(f"{i+1}: Eigenvalue = {val:.4f}")
    print(f"   Eigenvector (first 5 values): {vec[:5]}")
