from datetime import datetime
from typing import Optional
from sqlmodel import Field
from uuid import UUID
from core.schema import SchemaBase
from core.model import BaseModel


class UserCreaterSchema(SchemaBase):
    username: str = Field(..., max_length=64, description="用户名")
    nickname: str = Field(..., max_length=64, description="昵称")
    password: str = Field(..., max_length=255, description="密码")
    sex: int = Field(default=0, description="性别")
    avatar: str = Field(default='https://c-ssl.duitang.com/uploads/blog/202207/09/20220709150824_97667.jpg', max_length=255, description="头像")
    mobile: str = Field(..., max_length=11, description="手机号")
    is_active: int = Field(default=1, description="是否启用")
    is_superuser: int = Field(default=0, description="是否超级管理员")
    is_staff: int = Field(default=0, description="是否管理员")

class UserInfoOutSchema(SchemaBase):
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

    def model_dump(self):
        return {
            "id": str(self.id),
            "username": self.username,
            "nickname": self.nickname,
            "sex": self.sex,
            "avatar": self.avatar,
            "mobile": self.mobile,
            "is_active": self.is_active,
            "is_superuser": self.is_superuser,
            "is_staff": self.is_staff,
            "created_at":self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": self.updated_at.strftime("%Y-%m-%d %H:%M:%S")
        }


class UserListSchema(BaseModel):
    total: int = Field(..., description="总条数")
    list_data: list[UserInfoOutSchema] = Field(..., description="用户列表")
    current: int = Field(..., description="当前页")
    page_size: int = Field(..., description="每页条数")

    def model_dump(self):
        return {
            "total": self.total,
            "list_data": [user_info.model_dump() for user_info in self.list_data],  # 使用列表推导式调用model_dump
            "current": self.current,
            "page_size": self.page_size
        }


class UserSearchSchema(SchemaBase):
    current: int = Field(default=1, description="当前页")
    page_size: int = Field(default=10, description="每页条数")
    username: Optional[str] = Field(None, max_length=64, description="用户名")
    nickname: Optional[str] = Field(None, max_length=64, description="昵称")
    mobile: Optional[str] = Field(None, max_length=11, description="手机号")
    is_active: int = Field(default=1, description="是否启用")
    is_superuser: int = Field(default=0, description="是否超级管理员")
    is_staff: int = Field(default=0, description="是否管理员")
    begin_time: Optional[datetime] = Field(None, description="开始时间")
    end_time: Optional[datetime] = Field(None, description="结束时间")

class UserLoginSchema(SchemaBase):
    username: str = Field(..., max_length=64, description="用户名")
    password: str = Field(..., max_length=255, description="密码")

class UserResetPasswordSchema(SchemaBase):
    old_password: str = Field(..., max_length=255, description="密码")
    new_password: str = Field(..., max_length=255, description="新密码")