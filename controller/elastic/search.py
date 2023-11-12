from elasticsearch import Elasticsearch
from controller.pre_process import pre_process_element
import controller.elastic.formatting as ft
from datetime import date

client = Elasticsearch(
    'http://localhost:9200',
    basic_auth=['elastic', 'FGU_q6g_EjloOjrxAcsM']
)


def add_bulk_data():
    with open('../resources/new_ndjsonfile.json', 'r') as file:
        data = file.read()
    client.bulk(operations=data)


def search_by_all(query: str):
    print(pre_process_element(query))
    result = client.search(index='people-library', query={
        'match': {
            'all_combined': pre_process_element(query)
        }
    }, size=50)
    return ft.format_elastic_result(result)


def search_by_name(name: str):
    result = client.search(index='people-library', query={
        'match': {
            'Name': name
        }
    }, size=50)
    return ft.format_elastic_result(result)


def search_by_dob_range(mindate: date, maxdate: date):
    result = client.search(index='people-library', query={
        'range': {
            'Date of Birth': {
                'gte': mindate,
                'lte': maxdate
            }
        }
    }, size=50)
    return ft.format_elastic_result(result)


def search_by_occupation(occupation: str):
    result = client.search(index='people-library', query={
        'match': {
            '_occupation': pre_process_element(occupation)
        }
    }, size=50)
    return ft.format_elastic_result(result)


def search_multiline(filters: dict):
    queryList = []
    for filter in filters:
        queryList.append(
            {'match': { filter: filters[filter] } }
        )
    print(queryList)
    result = client.search(index='people-library', query={
        'bool': {
            'should': queryList
        }
    })
    return ft.format_elastic_result(result)


if __name__ == '__main__':
    print(search_multiline(
        {
            'Occupation' : 'Engineer'
        }
    ))
