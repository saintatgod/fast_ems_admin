from sqlmodel import Field, String, Integer, Boolean
from core.base_model import BaseModel

class User(BaseModel, table=True):
    """用户表"""
    __tablename__ = "user"

    username: str = Field(String, max_length=64, unique=True, description="用户名")
    nickname: str = Field(String, max_length=64, description="昵称")
    password: str = Field(String, max_length=255, description="密码")
    sex: int = Field(default=0, description="性别")
    avatar: str = Field(String, max_length=255, description="头像")
    mobile: str = Field(String, max_length=11, description="手机号")
    is_active: int = Field(default=1, description="是否启用")
    is_superuser: int = Field(default=0, description="是否超级管理员")
    is_staff: int = Field(default=0, description="是否管理员")
