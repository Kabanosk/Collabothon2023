from sklearn.feature_extraction.text import CountVectorizer

from .recommender_model import Model


def get_model(sql_data) -> Model:
    data = {}
    for el in sql_data:
        if el[0] in data:
            data[el[0]].append(str(el[1]))
        else:
            data[el[0]] = [str(el[1])]
    x_text = [" ".join(sublist) for sublist in data.values()]

    count_vectorizer = CountVectorizer(token_pattern=r"\b\d+\b")
    data_matrix = count_vectorizer.fit_transform(x_text).toarray()
    for i, k in enumerate(data):
        data[k] = data_matrix[i]
    return Model(data)
