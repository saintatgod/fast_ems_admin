from uuid import UUID

from sqlmodel import select, func

from core.databases import create_db_connect
from app.admin.models import User

class UserRepository:
    def __init__(self):
        # 创建数据库连接
        self.session = create_db_connect()
        # 模型类
        self.model = User

    async def get_user_by_id(self, user_id: UUID) -> dict:
        # 异步获取用户信息
        async with self.session() as session:
            # 查询用户信息
            result = await session.exec(select(User).where(User.id == user_id)).first()
            # 返回用户信息
            return result.dict()

    async def is_exist_by_username(self, username: str) -> bool:
        # 异步判断用户名是否存在
        async with create_db_connect()  as session:
            # 查询用户信息
            result = await session.execute(select(User).where(User.username == username))
            # 获取第一个结果
            user = result.scalars().first()
            # 返回是否存在
            return user is not None

    async def create_user(self, user: dict) -> dict:
        # 异步创建用户
        async with create_db_connect() as session:
            # 创建用户对象
            user_obj = User(**user)
            # 添加用户对象
            session.add(user_obj)
            # 提交事务
            await session.commit()
            # 返回用户信息
            return user_obj.dict()

    async def get_user_list(self, user_search: dict, page:int, page_size:int) -> list:
        # 查询用户列表
        query = select(User)
        # 根据用户名查询
        if user_search.get('username'):
            query = query.where(User.username == user_search.get('username'))
        # 根据昵称查询
        if user_search.get('nickname'):
            query = query.where(User.nickname == user_search.get('nickname'))
        # 根据手机号查询
        if user_search.get('mobile'):
            query = query.where(User.mobile == user_search.get('mobile'))
        # 根据是否激活查询
        if user_search.get('is_active'):
            query = query.where(User.is_active == user_search.get('is_active'))
        # 根据是否是超级用户查询
        if user_search.get('is_superuser'):
            query = query.where(User.is_superuser == user_search.get('is_superuser'))
        # 根据是否是管理员查询
        if user_search.get('is_staff'):
            query = query.where(User.is_staff == user_search.get('is_staff'))
        # 根据性别查询
        if user_search.get('sex'):
            query = query.where(User.sex == user_search.get('sex'))
        # 根据创建时间查询
        if user_search.get('start_time') and user_search.get('end_time'):
            query = query.where(User.created_at.between(user_search.get('start_time'), user_search.get('end_time')))

        # 异步获取用户列表
        async with create_db_connect() as session:
            # 查询用户列表
            result = await session.execute(query.limit(page_size).offset((page - 1) * page_size))
            # 返回用户列表
            return [item.dict() for item in result.scalars()]

    async def get_user_count(self, user_search: dict) -> int:
        # 查询用户数量
        query = select(func.count(User.id))
        # 根据用户名查询
        if user_search.get('username'):
            query = query.where(User.username == user_search.get('username'))
        # 根据昵称查询
        if user_search.get('nickname'):
            query = query.where(User.nickname == user_search.get('nickname'))
        # 根据手机号查询
        if user_search.get('mobile'):
            query = query.where(User.mobile == user_search.get('mobile'))
        # 根据是否激活查询
        if user_search.get('is_active'):
            query = query.where(User.is_active == user_search.get('is_active'))
        # 根据是否是超级用户查询
        if user_search.get('is_superuser'):
            query = query.where(User.is_superuser == user_search.get('is_superuser'))
        # 根据是否是管理员查询
        if user_search.get('is_staff'):
            query = query.where(User.is_staff == user_search.get('is_staff'))
        # 根据性别查询
        if user_search.get('sex'):
            query = query.where(User.sex == user_search.get('sex'))
        # 根据创建时间查询
        if user_search.get('start_time') and user_search.get('end_time'):
            query = query.where(User.created_at.between(user_search.get('start_time'), user_search.get('end_time')))

        # 异步获取用户数量
        async with create_db_connect() as session:
            # 查询用户数量
            result = await session.execute(query)
            # 返回用户数量
            return result.scalar()