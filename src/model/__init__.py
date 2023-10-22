import numpy as np

from database.utils import get_all_plants_from_db
from .recommender_model import Model


def get_model(sql_data) -> Model:
    data = {}
    num_of_plants = max(get_all_plants_from_db(), key=lambda x: x[1])

    for el in sql_data:
        if el[0] in data:
            data[el[0]][el[1]] += 1
        else:
            data[el[0]] = np.zeros(num_of_plants[0]*2)
            data[el[0]][el[1]] = 1
    m = Model(data)
    m.train()
    return m

