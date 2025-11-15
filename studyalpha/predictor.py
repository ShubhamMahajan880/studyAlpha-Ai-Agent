"""
Small ML predictor for weakness scoring.
Uses GradientBoostingClassifier trained on synthetic data for demo.
"""
import joblib
import numpy as np
from typing import List, Optional
from sklearn.ensemble import GradientBoostingClassifier
from .utils import trace

MODEL_PATH = "predictor_model.joblib"

def make_synthetic_training_data(n: int = 600):
    X = np.random.rand(n, 3)
    # y=1 means needs revision (weak)
    y = (X[:, 0] < 0.6).astype(int)
    return X, y

def train_and_save_model(path: str = MODEL_PATH):
    X, y = make_synthetic_training_data()
    clf = GradientBoostingClassifier(n_estimators=50)
    clf.fit(X, y)
    joblib.dump(clf, path)
    trace("predictor.train", {"path": path})
    return path

def load_model(path: str = MODEL_PATH) -> Optional[GradientBoostingClassifier]:
    try:
        return joblib.load(path)
    except Exception:
        trace("predictor.load_failed", {"path": path})
        return None

def predict_weakness(features: List[float], model: Optional[GradientBoostingClassifier] = None) -> float:
    if model is None:
        model = load_model()
    if model is None:
        # deterministic fallback heuristic
        prob = float(max(0.0, 0.95 - features[0]))
        trace("predictor.fallback", {"features": features, "prob": prob})
        return prob
    prob = float(model.predict_proba([features])[0][1])
    trace("predictor.predict", {"features": features, "prob": prob})
    return prob
