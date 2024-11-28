# -*- coding: utf-8 -*-
from uuid import UUID
from typing import Optional
from app.admin.repository.user import UserRepository
from app.admin.schemas.user import UserCreaterSchema, UserListSchema,UserInfoSchema
from utils.auth import Auth

class UserService:
    @staticmethod
    async def create_user(user: UserCreaterSchema)->UserInfoSchema:
        """创建用户"""
        new_user = user.dict()
        new_user['password'] = Auth.hash_password(new_user['password'])
        # 使用 setdefault 设置默认值
        new_user.setdefault('avatar', 'https://pic.616pic.com/ys_bnew_img/00/17/67/CtVmZbeZqv.jpg')
        new_user.setdefault('nickname', new_user['username'])
        new_user.setdefault('sex', 0)
        new_user.setdefault('is_active', 1)
        new_user.setdefault('is_superuser', 0)
        new_user.setdefault('is_staff', 0)
        new_user.setdefault('mobile', '')

        user_repo = UserRepository()
        new_user_info = await user_repo.create_user(new_user)
        return UserInfoSchema(**new_user_info)

    @staticmethod
    async def is_exist_by_username(username: str)->bool:
        """判断用户名是否存在"""
        user_repo = UserRepository()
        return await user_repo.is_exist_by_username(username)

    @staticmethod
    async def update_user(user_id: UUID, user: UserCreaterSchema)->Optional[UserInfoSchema]:
        """更新用户"""
        user_repo = UserRepository()
        user_info = await user_repo.get_user_by_id(user_id)
        if not user_info:
            return None
        user_info = await user_repo.update_user(user_id, user.dict())
        return UserInfoSchema(**user_info)

    @staticmethod
    async def reset_password(user_id: UUID, old_password: str, new_password)->UserInfoSchema:
        """重置密码"""
        user_repo = UserRepository()
        user_info = await user_repo.get_user_by_id(user_id)
        if new_password == old_password:
            raise Exception('新密码不能与旧密码相同')
        if not Auth.verify_password(old_password, user_info['password']):
            raise Exception('旧密码错误')
        user_info['password'] = Auth.hash_password(new_password)
        user_info = await user_repo.update_user(user_id, user_info)
        return UserInfoSchema(**user_info)

    @staticmethod
    async def get_user_by_id(user_id: UUID)->Optional[UserInfoSchema]:
        """根据id获取用户"""
        user_repo = UserRepository()
        user_info = await user_repo.get_user_by_id(user_id)
        if not user_info:
            return None
        return UserInfoSchema(**user_info)

    @staticmethod
    async def user_auth(username:str, password:str):
        """用户认证"""
        user_repo = UserRepository()
        user_info = await user_repo.get_user_by_username(username)
        if not user_info:
            raise Exception('用户不存在')
        if not Auth.verify_password(password, user_info['password']):
            raise Exception('密码错误')
        return user_info


    @staticmethod
    async def get_user_list(user_search)->UserListSchema:
        user_search = user_search.dict()
        page = max(user_search.get('page', 1), 1)
        page_size = max(user_search.get('page_size', 10), 1)

        user_repo = UserRepository()
        list_data = await user_repo.get_user_list(user_search, page, page_size)
        total = await user_repo.get_user_count(user_search)
        return UserListSchema(total=total, data=list_data, current=page, page_size=page_size)