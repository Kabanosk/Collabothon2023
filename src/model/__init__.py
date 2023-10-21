from sklearn.feature_extraction.text import CountVectorizer

from .recommender_model import Model

# def get_model(sql_data: list) -> Model:
#     x_text = [list(map(str, sublist)) for sublist in sql_data]
#     count_vectorizer = CountVectorizer()
#     data_matrix = count_vectorizer.fit_transform(x_text).toarray()
#     return Model(data_matrix)
