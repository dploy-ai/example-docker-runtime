import os

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import joblib
import pandas as pd


def train(model_location):
    iris = load_iris()
    data = pd.DataFrame(
        {
            "sepal length": iris.data[:, 0],
            "sepal width": iris.data[:, 1],
            "petal length": iris.data[:, 2],
            "petal width": iris.data[:, 3],
            "species": iris.target,
        }
    )

    X = data[["sepal length", "sepal width", "petal length", "petal width"]]
    y = data["species"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    clf = RandomForestClassifier(n_estimators=3)
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    print("Accuracy: {}".format(metrics.accuracy_score(y_test, y_pred)))

    joblib.dump(clf, model_location)
    print("Saved to: {}".format(model_location))


if __name__ == '__main__':
    _model_location = os.path.join("..", "model", "my_model.joblib")
    train(model_location=_model_location)
