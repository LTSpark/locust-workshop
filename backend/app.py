from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from controllers import company_router


tags_metadata = [
    {
        "name": "Companies",
        "description": "Manage Companies database operations"
    }
]

app = FastAPI(
    title="Workshop Companies Demo App",
    version="1.0.0",
    description="Demo REST API for Locust Workshop",
    docs_url="/api/v1/docs",
    openapi_tags=tags_metadata
)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(company_router, tags=["Companies"])
