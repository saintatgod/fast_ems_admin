from fastapi import APIRouter

user_router = APIRouter()

@user_router.get("/info")
async def get_user_info():
    return {"username": "admin", "avatar": "https://www.example.com/avatar.jpg"}