from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler

data = load_breast_cancer()
x = data.data
y = data.target

scaler = StandardScaler()
x = scaler.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

model = LogisticRegression(max_iter=1000, solver='saga')
model.fit(x_train, y_train)
print(model.get_params())

print(model.score(x_train, y_train))
print(model.score(x_test, y_test))

print(model.predict_proba(x_train))
print(model.predict_proba(x_test))
