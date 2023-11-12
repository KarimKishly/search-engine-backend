def format_elastic_result(elasticresult: dict):
    hits = elasticresult['hits']['hits']
    result = [{
        'score' : hit['_score'],
        'Name' : hit['_source']['Name'],
        'Gender' : hit['_source']['Gender'],
        'Age' : hit['_source']['Age'],
        'DOB' : hit['_source']['Date of Birth'],
        'Description' : hit['_source']['Description'],
        'Occupation' : hit['_source']['Occupation'],
        'Interests' : hit['_source']['Interests'],
        'Likes' : hit['_source']['Likes']
    } for hit in hits]
    return result

if __name__ == '__main__':
    print("")