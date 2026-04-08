import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets
from sklearn.metrics import accuracy_score

# load dataset
iris = datasets.load_iris()

X = iris.data
y = iris.target

# split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# create model
knn = KNeighborsClassifier(n_neighbors=3)

# train model
knn.fit(X_train, y_train)

# prediction
y_pred = knn.predict(X_test)

# accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

# new prediction
new_flower = [[5.1, 3.5, 1.4, 0.2]]
prediction = knn.predict(new_flower)
print("Flower name:", iris.target_names[prediction][0])