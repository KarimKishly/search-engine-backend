import json

def format_ndjson(index: str, data: list):
    ndjson_data = []
    if isinstance(data, list):
        for element in data:
            ndjson_data.append({'index' : {'_index' : index}})
            ndjson_data.append(element)
    elif isinstance(data, dict):
        ndjson_data.append({'index': {'_index': index}})
        ndjson_data.append(data)
    return ndjson_data
def create_ndjson_file(index: str, data: list):
    ndjson_data = format_ndjson(index, data)
    ndjson_file = ''
    for element in ndjson_data:
        ndjson_file = ndjson_file + json.dumps(element) + '\n'
    return ndjson_file

if __name__ == '__main__':
    with open('../generating_documents/resources/people_dataset.json', 'r') as file:
        data = json.load(file)
    # ndjson_data = format_ndjson('people', data)
    with open('resources/ndjsonfile.json', 'w') as file:
        file.write(create_ndjson_file('people-library', data))

