import json
from sklearn.feature_extraction.text import CountVectorizer

with open('resources/base_data_filtered.json', 'r') as file:
    original_documents = json.load(file)

all_documents_text = []

for document in original_documents:
    text = document['all_combined']
    all_documents_text.append(text)

with open('resources/feature_names.txt', 'w') as file:
    file.write('@'.join(all_documents_text))

vectorizer = CountVectorizer()
vectorizer.fit(all_documents_text)

vectorized_documents = {}
for index, document in enumerate(original_documents):
    text = document['all_combined']  # Modify this based on the structure of your documents
    vectorized_document = vectorizer.transform([text]).toarray()[0]
    vectorized_documents[str(index)] = vectorized_document.tolist()

with open('resources/tf_vectorized_documents.json', 'w') as file:
    json.dump(vectorized_documents, file)