import numpy as np
import pickle
import os


# We load the model once and cache it to make the app faster and more efficient

_model_cache = {}

def load_model():
    if "model" in _model_cache:
        return _model_cache["model"]

    filepath = os.path.join("models", "random_forest.pkl")   # Set path
    with open(filepath, "rb") as f:
        _model_cache["model"] = pickle.load(f)   # Load model with pickle

    return _model_cache["model"]


def predict(features: dict):
    """
    Function to predict whether a Pokémon is Legendary or not.
    Input: dictionary with the different features and their values.
    """

    model = load_model()

    X = np.array([[features["hit_points"], features["attack"], features["defense"],
                   features["sp_attack"], features["sp_defense"], features["speed"]]])

    y_pred = model.predict(X)[0]   # Prediction
    y_prob = model.predict_proba(X)[0][1]   # Probability of being Legendary

    return int(y_pred), float(y_prob)