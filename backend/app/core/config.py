from pathlib import Path
from pydantic import  PostgresDsn, validator
from typing import Any, Dict, List, Optional, Union
from pydantic_settings import BaseSettings

# 定义一个Settings类，继承自BaseSettings
class Settings(BaseSettings):
    # 项目根目录
    BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent
    # 是否开启调试模式
    DEBUG: bool = False
    # 服务器主机地址
    SERVER_HOST: str = "0.0.0.0"
    # 服务器端口号
    SERVER_PORT: int = 8000
    # API前缀
    API_PREFIX: str = "/api"

    # 是否开启SQL数据库
    SQL_DB_ENABLE: bool = True
    # SQL数据库连接URL
    SQL_DB_URL: Optional[PostgresDsn] = "postgresql://postgres:postgres@localhost:5432/postgres"

    # 接口文档标题
    TITLE: str = "EMS管理后台接口文档"
    # 接口文档版本
    VERSION: str = "0.0.1"
    # 接口文档描述
    DESCRIPTION: str = "EMS管理后台接口文档,基于FastAPI构建"

    # 获取后端属性
    @property
    def get_backend_attributes(self) -> Dict[str, Any]:
        return {
            "debug": self.DEBUG,
            "title": self.TITLE,
            "version": self.VERSION,
            "description": self.DESCRIPTION,
        }

# 实例化Settings类
settings = Settings()