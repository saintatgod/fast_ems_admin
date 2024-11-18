from uuid import UUID

from sqlmodel import select

from core.databases import create_db_connect
from app.admin.models import User

class UserRepository:
    def __init__(self):
        self.db = create_db_connect()

    async def get_user_by_id(self, user_id: UUID) -> dict:
        with self.db as session:
            result = session.exec(select(User).where(User.id == user_id)).first()
            return result.dict()

    async def create_user(self, user: dict) -> dict:
        with self.db as session:
            session.add(User(**user))
            session.commit()
            session.refresh(user)
            return user.dict()