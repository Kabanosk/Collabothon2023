from sklearn.neighbors import NearestNeighbors
import numpy as np


class Model:
    def __init__(self, data: np.array, n: int = 5):
        self.model = NearestNeighbors(n_neighbors=n, metric='cosine')
        self.data = data

    def train(self):
        self.model.fit(self.data)

    def add_user(self, user_data: np.array):
        self.data = np.vstack((self.data, user_data))
        self.train()

    def add_plant(self):
        n = len(self.data)
        self.data = np.hstack((self.data, np.zeros((n, 1))))
        self.train()

    def get_recommended_users(self, data: np.array, users: int=5) -> np.array:
        _, indices = self.model.kneighbors(data, n_neighbors=users)
        return indices

