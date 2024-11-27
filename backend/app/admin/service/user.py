# -*- coding: utf-8 -*-
from app.admin.repository.user import UserRepository
from app.admin.schemas.user import UserCreaterSchema, UserListSchema
from utils.auth import Auth

class UserService:
    @staticmethod
    async def create_user(user: UserCreaterSchema):
        """创建用户"""
        new_user = user.dict()
        new_user['password'] = Auth.hash_password(new_user['password'])
        if new_user.get('avatar') == '':
            new_user['avatar'] = 'https://pic.616pic.com/ys_bnew_img/00/17/67/CtVmZbeZqv.jpg'
        if new_user.get('nickname') == '':
            new_user['nickname'] = new_user['username']
        if new_user.get('sex') is None:
            new_user['sex'] = 0
        if new_user.get('is_active') is None:
            new_user['is_active'] = 1
        if new_user.get('is_superuser') is None:
            new_user['is_superuser'] = 0
        if new_user.get('is_staff') is None:
            new_user['is_staff'] = 0
        if new_user.get('mobile') is None:
            new_user['mobile'] = ''
        user_repo = UserRepository()
        return await user_repo.create_user(new_user)

    @staticmethod
    async def is_exist_by_username(username: str)->bool:
        """判断用户名是否存在"""
        user_repo = UserRepository()
        return await user_repo.is_exist_by_username(username)

    @staticmethod
    async def get_user_list(user_search)->UserListSchema:
        user_search = user_search.dict()
        """获取用户列表"""
        if isinstance(user_search.get('page'), int) and user_search.get('page') > 0:
            page = user_search.get('page')
        else:
            page = 1

        if isinstance(user_search.get('page_size'), int) and user_search.get('page_size') > 0:
            page_size = user_search.get('page_size')
        else:
            page_size = 10

        user_repo = UserRepository()
        list_data = await user_repo.get_user_list(user_search, page, page_size)
        total = await user_repo.get_user_count(user_search)
        return UserListSchema(total=total, data=list_data, current=page, page_size=page_size)