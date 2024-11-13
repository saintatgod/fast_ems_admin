from sqlmodel import Field, String, Integer, Boolean
from backend.core.base_model import BaseModel

class User(BaseModel):
    """用户表"""
    username: str = Field(String, max_length=64, unique=True, description="用户名")
    password: str = Field(String, max_length=256, description="密码")
    salt: str = Field(String, max_length=64, description="盐值")
    avatar: str = Field(String, max_length=256, description="头像")
    mobile: str = Field(String, max_length=11, description="手机号")
    is_active: bool = Field(Integer, default=1, description="是否启用")
    is_superuser: bool = Field(Integer, default=0, description="是否超级管理员")
    is_staff: bool = Field(Integer, default=0, description="是否管理员")