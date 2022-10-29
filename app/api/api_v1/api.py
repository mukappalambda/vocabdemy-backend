from app.api.api_v1.endpoints import users, vocabs
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(vocabs.router, prefix="/vocabs", tags=["vocabs"])
