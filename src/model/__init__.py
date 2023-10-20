import numpy as np

from .recommender_model import Model


def get_model(sql_data: list) -> Model:
    data = np.array(sql_data)
    return Model(data)
