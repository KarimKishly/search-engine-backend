from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from routes import search, upload

tags_metadata = [
    {
        "name": "Search",
        "description": "Use search engine",
    },
    {
        "name": "Upload",
        "description": "Upload docx files to search engine indexes"
    }
]

app = FastAPI(version='1.0', title='Search Engine Backend',
              description="API that interacts with elasticsearch in order to produce a functional search engine",
              openapi_tags=tags_metadata)

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],
                   )

app.include_router(
    search.router,
    prefix="/search",
    tags=["Search"],
    responses={404: {"description": "Not found"}}
)
app.include_router(
    upload.router,
    prefix="/upload",
    tags=["Upload"],
    responses={404: {"description": "Not found"}}
)
