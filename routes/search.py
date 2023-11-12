from fastapi import APIRouter, Request
import controller.elastic.search as es
from datetime import date
import custom_engine.tf_query as ce_tf
import custom_engine.idf_query as ce_idf

router = APIRouter()

@router.get('/all')
async def search_by_all_combined(q: str = None):
    return es.search_by_all(q)

@router.get('')
async def search_by_parameter(name: str = None, occupation: str = None):
    if name is not None:
        return es.search_by_name(name)
    if occupation is not None:
        return es.search_by_occupation(occupation)

@router.get('/dob')
async def search_by_date_of_birth_range(mindate: date, maxdate: date):
    try:
        return es.search_by_dob_range(mindate, maxdate)
    except:
        return []
@router.post('/multiline')
async def search_by_multiple_filters(request: Request):
    filters = await request.json()
    return es.search_multiline(filters)

@router.get('/tf')
async def search_by_tf_only(q: str = None):
    return ce_tf.search_by_tf_only(q)

@router.get('/idf')
async def search_by_idf_only(q: str = None):
    return ce_idf.search_by_idf_only(q)
