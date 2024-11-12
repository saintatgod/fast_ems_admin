from fastapi import APIRouter
from .api import api_router

admin_router = APIRouter()
admin_router.include_router(api_router, prefix="/admin")