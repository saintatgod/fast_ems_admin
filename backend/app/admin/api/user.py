from fastapi import APIRouter, Request

from app.admin.schemas.user import UserCreaterSchema,UserListSchema,UserSearchSchema
from app.admin.service.user import UserService

user_router = APIRouter()

@user_router.post("/create")
async def create_user(user: UserCreaterSchema):
    is_existed = await UserService.is_exist_by_username(user.username)
    if is_existed:
        return {"message": "用户已存在"}
    return await UserService.create_user(user)

@user_router.get("/list")
async def list_user(user_search: UserSearchSchema):
    return await UserService.get_user_list(user_search)