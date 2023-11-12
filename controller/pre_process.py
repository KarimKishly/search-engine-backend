import json
import hashlib
import random
import math
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from datetime import datetime



def pre_process_file(file):
    all_entries = file.split('\n')
    new_ndjson = ''
    index = 0
    while index < file.count('\n'):
        elastic_index = all_entries[index]
        entry = all_entries[index+1]
        all = pre_process_entry(entry)
        entry = json.loads(entry)
        entry['all_combined'] = all
        id = generate_id()
        entry['id'] = id
        entry['_occupation'] = pre_process_element(entry['Occupation'])
        new_ndjson = new_ndjson + elastic_index + '\n' + json.dumps(entry) + '\n'
        index += 2
    return new_ndjson

def pre_process_entry(entry):
    entry = json.loads(entry)
    all_entry = []
    for key in entry:
        if key != 'Date of Birth':
            no_stopwords = remove_stopwords(str(entry[key]))
            stemmed = stem_text(no_stopwords)
            all_entry.append(stemmed)
        else:
            all_entry.append(entry[key])
            all_entry.append(iso_to_english(entry[key]))
    all_entry = ' / '.join(all_entry)
    return all_entry

def pre_process_element(element: str):
    no_stopwords = remove_stopwords(element)
    stemmed = stem_text(no_stopwords)
    return stemmed

def remove_stopwords(text):
    tokens = word_tokenize(text)

    stop_words = set(stopwords.words('english'))
    stop_words.add('.')

    filtered_tokens = [token for token in tokens if token.lower() not in stop_words]

    filtered_text = ' '.join(filtered_tokens)

    return filtered_text
def iso_to_english(iso_date):
    date_obj = datetime.fromisoformat(iso_date)

    english_date = date_obj.strftime("%B %d, %Y")

    return pre_process_element(english_date.lower())

def stem_text(text):
    from nltk.stem import PorterStemmer
    from nltk.tokenize import word_tokenize

    stemmer = PorterStemmer()

    words = word_tokenize(text)

    stemmed_words = [stemmer.stem(word) for word in words]

    stemmed_string = " ".join(stemmed_words)

    return stemmed_string
def generate_id():
    random_number = random.randint(1, math.pow(10,12))
    number_bytes = str(random_number).encode('utf-8')
    sha256_hash = hashlib.sha256()
    sha256_hash.update(number_bytes)
    hashed_number = sha256_hash.hexdigest()
    hashed_number = hashed_number[0:20]

    return hashed_number

if __name__ == '__main__':

    with open('resources/ndjsonfile.json', 'r') as file_read:
        file = file_read.read()
    with open('resources/new_ndjsonfile.json', 'w') as f:
        f.write(pre_process_file(file))


