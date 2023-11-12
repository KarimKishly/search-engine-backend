from fastapi import APIRouter, UploadFile, File
from controller.ndjson_format import create_ndjson_file
from generating_documents.docx_to_json import docx_to_json
from controller.pre_process import pre_process_file
from elasticsearch import Elasticsearch
import json

client = Elasticsearch(
    'http://localhost:9200',
    basic_auth=['elastic', 'FGU_q6g_EjloOjrxAcsM']
)

router = APIRouter()

@router.post('')
async def upload_docx_file(file: UploadFile = File(...)):
    with open('resources/tempfile.docx', 'wb') as f:
        f.write(await file.read())
    index = 'people-library'
    json_file = docx_to_json('resources/tempfile.docx')
    ndjson_file = create_ndjson_file(index, json_file)
    ndjson_file_pp = pre_process_file(ndjson_file)
    client.bulk(operations=ndjson_file_pp)
    return {"status" : 200}
