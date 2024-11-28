from fastapi import APIRouter, Request
from uuid import UUID
from app.admin.schemas.user import UserCreaterSchema,UserListSchema,UserSearchSchema, UserLoginSchema,UserResetPasswordSchema
from app.admin.service.user import UserService
from sqlalchemy import result_tuple

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

@user_router.get("/detail/{user_id}")
async def get_user_detail(user_id: UUID):
    return await UserService.get_user_by_id(user_id)

@user_router.post("/update/{user_id}")
async def update_user(user_id: UUID, user: UserCreaterSchema):
    return await UserService.update_user(user_id, user)

@user_router.post("/login")
async def login_user(user: UserLoginSchema):
    try:
        user_info = await UserService.user_auth(user.username, user.password)
        if user_info:
            return user_info
    except Exception as e:
        return {"message": str(e)}

@user_router.post("/logout")
async def logout_user(request: Request):
    return await UserService.logout_user(request)

@user_router.post("/reset_password")
async def reset_password(user_id: UUID, user: UserResetPasswordSchema):
    if not user.old_password or not user.new_password:
        return {"message": "请输入旧密码和新密码"}
    try:
        result = await UserService.reset_password(user_id, old_password=user.old_password, new_password=user.new_password)
        if result:
            return {"message": "密码修改成功"}
    except Exception as e:
        return {"message": str(e)}