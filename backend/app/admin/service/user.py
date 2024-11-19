# -*- coding: utf-8 -*-
from app.admin.repository.user import UserRepository
from app.admin.schemas.user import UserCreate, UserInfo
from utils.auth import Auth

class UserService:
    @staticmethod
    async def create_user(user: UserCreate):
        new_user = user.dict()
        new_user['salt'] = '111'
        new_user['password'] = Auth.hash_password(new_user['password'])
        user_repo = UserRepository()
        return await user_repo.create_user(new_user)