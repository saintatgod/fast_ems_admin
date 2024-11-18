from datetime import datetime

from core.schema import SchemaBase

class UserCreate(SchemaBase):
    username: str
    password: str
    avatar: str|None = None
    mobile: str
    is_staff: int = 0
    is_superuser: int = 0
    is_active: int = 1

class UserInfo(SchemaBase):
    id: int
    username: str
    avatar: str|None = None
    mobile: str
    is_staff: int = 0
    is_superuser: int = 0
    is_active: int = 1