import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from controller.pre_process import pre_process_element


def search_by_idf_only(query: str):
    with open('custom_engine/resources/base_data_filtered.json', 'r') as file:
        original_documents = json.load(file)

    with open('custom_engine/resources/feature_names.txt', 'r') as file:
        all_documents_text = file.read().split('@')

    vectorizer = TfidfVectorizer(use_idf=True, smooth_idf=False, sublinear_tf=False)
    vectorizer.fit(all_documents_text)

    with open('custom_engine/resources/idf_vectorized_documents.json', 'r') as file:
        vectorized_documents = json.load(file)
    query = pre_process_element(query)
    query_vector = vectorizer.transform([query]).toarray()[0]

    similarities = {}
    for index, vector in vectorized_documents.items():
        vector = np.array(vector)
        similarity = cosine_similarity([query_vector], [vector])[0][0]
        similarities[index] = similarity

    top_50 = sorted(similarities.items(), key=lambda x: x[1], reverse=True)[:50]

    most_similar_documents = []
    for index, similarity in top_50:
        document = original_documents[int(index)]
        document['score'] = "{:.5f}".format(similarity)
        del document['all_combined']
        if(similarity > 0.0):
            most_similar_documents.append(document)

    return most_similar_documents
