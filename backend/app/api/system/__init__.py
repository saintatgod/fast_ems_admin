from fastapi import APIRouter
from .user import router as user_router

system_router = APIRouter()
system_router.include_router(user_router, prefix="/user", tags=["用户模块"])