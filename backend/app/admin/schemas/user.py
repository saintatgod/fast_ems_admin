from datetime import datetime
from sqlmodel import Field
from uuid import UUID
from core.schema import SchemaBase


class UserCreaterSchema(SchemaBase):
    username: str = Field(..., max_length=64, description="用户名")
    nickname: str = Field(..., max_length=64, description="昵称")
    password: str = Field(..., max_length=255, description="密码")
    sex: int = Field(default=0, description="性别")
    avatar: str = Field(..., max_length=255, description="头像")
    mobile: str = Field(..., max_length=11, description="手机号")
    is_active: int = Field(default=1, description="是否启用")
    is_superuser: int = Field(default=0, description="是否超级管理员")
    is_staff: int = Field(default=0, description="是否管理员")

class UserInfoSchema(SchemaBase):
    id: UUID = Field(..., description="用户ID")
    username: str = Field(..., max_length=64, description="用户名")
    nickname: str = Field(..., max_length=64, description="昵称")
    sex: int = Field(default=0, description="性别")
    avatar: str = Field(..., max_length=255, description="头像")
    mobile: str = Field(..., max_length=11, description="手机号")
    is_active: int = Field(default=1, description="是否启用")
    is_superuser: int = Field(default=0, description="是否超级管理员")
    is_staff: int = Field(default=0, description="是否管理员")
    created_at: datetime = Field(..., description="创建时间")
    updated_at: datetime = Field(..., description="更新时间")

class UserListSchema(SchemaBase):
    total: int = Field(..., description="总条数")
    data: list[UserInfoSchema] = Field(..., description="用户列表")
    current: int = Field(..., description="当前页")
    page_size: int = Field(..., description="每页条数")

class UserSearchSchema(SchemaBase):
    current: int = Field(..., description="当前页")
    page_size: int = Field(..., description="每页条数")
    username: str = Field(None, max_length=64, description="用户名")
    nickname: str = Field(None, max_length=64, description="昵称")
    mobile: str = Field(None, max_length=11, description="手机号")
    is_active: int = Field(default=1, description="是否启用")
    is_superuser: int = Field(default=0, description="是否超级管理员")
    is_staff: int = Field(default=0, description="是否管理员")
    start_time: datetime = Field(..., description="创建时间-开始")
    end_time: datetime = Field(..., description="创建时间-结束")

class UserLoginSchema(SchemaBase):
    username: str = Field(..., max_length=64, description="用户名")
    password: str = Field(..., max_length=255, description="密码")

class UserResetPasswordSchema(SchemaBase):
    old_password: str = Field(..., max_length=255, description="密码")
    new_password: str = Field(..., max_length=255, description="新密码")