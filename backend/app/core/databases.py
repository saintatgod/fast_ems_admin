from fastapi import FastAPI
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
    AsyncEngine
)
from app.core.config import settings
from app.core.exceptions import CustomException

def create_db_connect() -> async_sessionmaker:
    if not settings.SQL_DB_TYPE:
        raise CustomException(msg="请先配置数据库链接并选择使用的数据库类型", desc="请启用 app/core/config.py: SQL_DB_TYPE")

    match settings.SQL_DB_TYPE:
        case "postgresql":
            async_engine = create_pgsql_engine()
        case "sqlite":
            async_engine = create_sqlite_engine()
        case _:
            raise CustomException(msg="请先配置数据库链接并选择使用的数据库类型", desc="请启用 app/core/config.py: SQL_DB_TYPE")

    session_factory = async_sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=async_engine,
        expire_on_commit=False,
        class_=AsyncSession
    )
    return session_factory()

def create_pgsql_engine()->AsyncEngine:
    return create_async_engine(
        settings.SQL_PGSQL_URL.unicode_string(),
        pool_size=20,  # 连接数
        max_overflow=10,  # 超出连接数时，允许再新建的连接数
        pool_timeout=30,  # 等待可用连接时间，超时则报错，默认为30秒
        pool_recycle=60,  # 连接生存时长，超过则该连接被回收，再生存新连接
        echo=False,
        echo_pool=False,
        pool_pre_ping=True,
        future=True
    )

def create_sqlite_engine()->AsyncEngine:
    return create_async_engine(settings.SQLITE_DB_URL.unicode_string(), echo=False, future=True)