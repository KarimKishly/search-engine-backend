import json

from elasticsearch import Elasticsearch

from controller.ndjson_format import create_ndjson_file
from controller.pre_process import pre_process_file

client = Elasticsearch(
    'http://localhost:9200',
    basic_auth=['elastic', 'FGU_q6g_EjloOjrxAcsM']
)

if __name__ == '__main__':

    with open('../../generating_documents/resources/people_dataset.json', 'r') as file:
        data = json.loads(file.read())
    default_index_name = 'people-library'

    client.indices.delete(index=default_index_name)

    print(client.indices.create(index=default_index_name))

    ndjson_file = create_ndjson_file(default_index_name, data)
    ndjson_file_pp = pre_process_file(ndjson_file)

    print(client.bulk(operations=ndjson_file_pp))
