from uuid import UUID

from sqlmodel import select

from core.databases import create_db_connect
from app.admin.models import User

class UserRepository:
    def __init__(self):
        self.session = create_db_connect()
        self.model = User

    async def get_user_by_id(self, user_id: UUID) -> dict:
        async with self.session() as session:
            result = await session.exec(select(User).where(User.id == user_id)).first()
            return result.dict()

    async def create_user(self, user: dict) -> dict:
        async with create_db_connect() as session:
            user_obj = User(**user)
            session.add(user_obj)
            await session.commit()
            return user_obj.dict()
