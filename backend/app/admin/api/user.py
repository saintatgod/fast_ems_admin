from fastapi import APIRouter, Request

from app.admin.schemas.user import UserCreate, UserInfo
from app.admin.service.user import UserService

user_router = APIRouter()

@user_router.get("/info")
async def get_user_info():
    return {"username": "admin", "avatar": "https://www.example.com/avatar.jpg"}

@user_router.post("/create")
async def create_user(user: UserCreate, request: Request):
    return await UserService.create_user(user)