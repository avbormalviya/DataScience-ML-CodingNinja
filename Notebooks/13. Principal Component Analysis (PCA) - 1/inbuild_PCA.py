from sklearn.datasets import load_breast_cancer
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# Load dataset
cancer = load_breast_cancer()


# Scale features
def scale_data(data):
    return StandardScaler().fit_transform(data)


# Train and evaluate Logistic Regression
def train_and_evaluate(x_train, x_test, y_train, y_test):
    model = LogisticRegression(max_iter=1000)
    model.fit(x_train, y_train)
    return model.score(x_test, y_test)


def best_k(x_train):
    pca = PCA()
    pca.fit(x_train)

    total = sum(pca.explained_variance_)
    variance = 0
    k = 0

    while variance / total < 0.9:
        variance += pca.explained_variance_[k]
        k += 1

    return k


# Apply PCA
def apply_pca(x_train, x_test, n_components=15):
    pca = PCA(n_components=best_k(x_train))
    return pca.fit_transform(x_train), pca.transform(x_test)


# Prepare data
x_scaled = scale_data(cancer.data)
x_train, x_test, y_train, y_test = train_test_split(x_scaled, cancer.target, random_state=42)

# Without PCA
score_no_pca = train_and_evaluate(x_train, x_test, y_train, y_test)
print("Accuracy without PCA:", score_no_pca)

# With PCA
x_train_pca, x_test_pca = apply_pca(x_train, x_test)
score_pca = train_and_evaluate(x_train_pca, x_test_pca, y_train, y_test)
print("Accuracy with PCA:", score_pca)
