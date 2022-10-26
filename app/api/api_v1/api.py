from app.api.api_v1.endpoints import vocabs
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(vocabs.router, prefix="/vocabs", tags=["vocabs"])
