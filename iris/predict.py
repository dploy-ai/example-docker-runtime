import joblib
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_location = os.path.join(ROOT_DIR, "model", "my_model.joblib")
clf = joblib.load(model_location)


def predict(X: list) -> list:
    return clf.predict(X).tolist()
