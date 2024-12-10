from fastapi import APIRouter, Request, Depends
from uuid import UUID
from app.admin.schemas.user import (
    UserCreaterSchema,
    UserInfoOutSchema,
    UserSearchSchema,
    UserLoginSchema,
    UserResetPasswordSchema,
)
from app.admin.service.user import UserService
from core.response import SuccessResponse, ErrorResponse

user_router = APIRouter()

@user_router.post("/create")
async def create_user(user: UserCreaterSchema = Depends(UserCreaterSchema)):
    is_existed = await UserService.is_exist_by_username(user.username)
    if is_existed:
        return SuccessResponse(msg="用户名已存在")
    user_info = await UserService.create_user(user)
    return SuccessResponse(data=user_info, msg="创建用户成功")

@user_router.get("/list")
async def list_user(user_search: UserSearchSchema = Depends(UserSearchSchema)):
    list_data = await UserService.get_user_list(user_search)
    return SuccessResponse(data=list_data)

@user_router.get("/detail/{user_id}")
async def get_user_detail(user_id: UUID):
    user_info = await UserService.get_user_by_id(user_id)
    return SuccessResponse(data=user_info, msg="获取用户详情成功")

@user_router.post("/update/{user_id}")
async def update_user(user_id: UUID, user: UserCreaterSchema = Depends(UserCreaterSchema)):
    user_info = await UserService.update_user(user_id, user)
    return SuccessResponse(data=user_info, msg="更新用户成功")

@user_router.post("/login")
async def login_user(user: UserLoginSchema = Depends(UserLoginSchema)):
    try:
        user_info = await UserService.user_auth(user.username, user.password)
        if user_info:
            return SuccessResponse(data=user_info, msg="登录成功")
    except Exception as e:
        return ErrorResponse(msg=str(e))

@user_router.post("/logout")
async def logout_user(request: Request):
    result = await UserService.logout_user(request)
    return SuccessResponse(msg="登出成功")

@user_router.post("/reset_password")
async def reset_password(user_id: UUID, user: UserResetPasswordSchema = Depends(UserResetPasswordSchema)):
    if not user.old_password or not user.new_password:
        return ErrorResponse(msg="请输入旧密码和新密码")
    try:
        result = await UserService.reset_password(user_id, old_password=user.old_password, new_password=user.new_password)
        if result:
            return SuccessResponse(msg="密码重置成功")
    except Exception as e:
        return ErrorResponse(msg=str(e))
