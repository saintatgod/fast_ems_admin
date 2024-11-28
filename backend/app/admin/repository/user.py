from uuid import UUID

from sqlmodel import select, update, func, and_
from app.admin.models import User
from core.databases import create_db_connect

class UserRepository:
    def __init__(self):
        self.db_session = create_db_connect()
        self.model = User

    async def get_user_by_id(self, user_id: UUID) -> dict:
        result = await self.db_session.execute(select(self.model).where(self.model.id == user_id))
        user = result.scalars().first()
        return user.dict() if user else {}

    async def get_user_by_username(self, username: str) -> dict:
        result = await self.db_session.execute(select(self.model).where(self.model.username == username))
        user = result.scalars().first()
        return user.dict() if user else {}

    async def is_exist_by_username(self, username: str) -> bool:
        result = await self.db_session.scalar(select(func.count(self.model.id)).where(self.model.username == username))
        return result > 0

    async def create_user(self, user_data: dict) -> dict:
        user_obj = self.model(**user_data)
        self.db_session.add(user_obj)
        await self.db_session.commit()
        return user_obj.dict()

    async def update_user(self, user_id: UUID, user_data: dict) -> dict:
        restlt = await self.db_session.execute(update(self.model).where(self.model.id == user_id).values(**user_data))
        await self.db_session.commit()
        if restlt.rowcount > 0:
            return await self.get_user_by_id(user_id)
        return {}

    async def get_user_list(self, user_search: dict, page: int, page_size: int) -> list:
        query = select(self.model).where(self._build_query(user_search))
        result = await self.db_session.execute(query.limit(page_size).offset((page - 1) * page_size))
        return [item.dict() for item in result.scalars()]

    async def get_user_count(self, user_search: dict) -> int:
        query = select(func.count(self.model.id)).where(self._build_query(user_search))
        result = await self.db_session.scalar(query)
        return result

    def _build_query(self, user_search: dict):
        conditions = []

        if user_search.get('username'):
            conditions.append(self.model.username == user_search['username'])
        if user_search.get('nickname'):
            conditions.append(self.model.nickname == user_search['nickname'])
        if user_search.get('mobile'):
            conditions.append(self.model.mobile == user_search['mobile'])
        if user_search.get('is_active') is not None:
            conditions.append(self.model.is_active == user_search['is_active'])
        if user_search.get('is_superuser') is not None:
            conditions.append(self.model.is_superuser == user_search['is_superuser'])
        if user_search.get('is_staff') is not None:
            conditions.append(self.model.is_staff == user_search['is_staff'])
        if user_search.get('sex') is not None:
            conditions.append(self.model.sex == user_search['sex'])
        if user_search.get('start_time') and user_search.get('end_time'):
            conditions.append(self.model.created_at.between(user_search['start_time'], user_search['end_time']))

        return and_(*conditions) if conditions else True