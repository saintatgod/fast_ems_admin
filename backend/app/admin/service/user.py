# -*- coding: utf-8 -*-

from fastapi import Request

from app.admin.models.user import User
from app.admin.repository.user import UserRepository
from app.admin.schemas.user import UserCreate, UserInfo

class UserService:
    @staticmethod
    async def create_user(user: UserCreate, request: Request):
        user_repo = UserRepository()
        print(request)
        exit(11)
        user = await user_repo.create_user(user)
        return user