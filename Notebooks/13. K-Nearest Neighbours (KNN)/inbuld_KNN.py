import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.datasets import load_breast_cancer
from sklearn.neighbors import KNeighborsClassifier

# Load data
cancer = load_breast_cancer()

X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, random_state=42)

x_axis = list(range(1, 20, 2))  # 1, 3, 5, ..., 19
y_axis = []

# Cross-validation for different K
for k in x_axis:
    knn = KNeighborsClassifier(n_neighbors=k)
    cvs = cross_val_score(knn, X_train, y_train, cv=KFold(n_splits=5, shuffle=True, random_state=42))
    y_axis.append(cvs.mean())

# Find best K
best_k = x_axis[y_axis.index(max(y_axis))]

# Plot
plt.plot(x_axis, y_axis, "-c", linewidth=3, marker='o')
plt.title(f"Best K = {best_k}", fontsize=14)
plt.xticks(x_axis)
plt.xlabel("K (Number of Neighbors)")
plt.ylabel("Cross-Validation Accuracy")
plt.grid()
plt.show()

# Final model with best K
knn = KNeighborsClassifier(n_neighbors=best_k)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

print(f"Best K: {best_k}")
print(f"Test Accuracy: {knn.score(X_test, y_test):.4f}")
