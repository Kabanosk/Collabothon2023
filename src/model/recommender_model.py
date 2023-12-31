import joblib
import numpy as np
from sklearn.neighbors import NearestNeighbors


class Model:
    def __init__(self, data: dict, n: int = 5):
        self.model = NearestNeighbors(n_neighbors=n, metric="cosine")
        self.data = data

    def train(self):
        self.model.fit(list(self.data.values()))

    def add_plant(self):
        n = len(self.data)
        self.data = np.hstack((self.data, np.zeros((n, 1))))
        self.train()

    def get_recommended_users(self, data: np.array, users: int = 5) -> np.array:
        _, indices = self.model.kneighbors(data, n_neighbors=users)
        return indices

    def save(self):
        joblib.dump(self, "model.pkl")

    @classmethod
    def load(cls):
        return joblib.load("model.pkl")
